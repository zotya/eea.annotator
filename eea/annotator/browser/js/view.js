if(!jQuery.fn.addBack){
  jQuery.fn.addBack = jQuery.fn.andSelf;
}

if(window.EEA === undefined){
  var EEA = {
    who: 'eea.annotator',
    version: '1.0'
  };
}

EEA.AnnotatorUtil = {
  userString: function(user){
    if(user && user.name && user.id){
      return '@' + user.id + ' (' + user.name + ')';
    }
    return user;
  }
};

EEA.Annotator = function(context, options){
  var self = this;
  self.context = context;
  self.target = jQuery('#content');

  self.settings = {
    readOnly: self.context.data('readonly') || 0,
    prefix: '',
    user: {
      id: 'anonymous',
      name: 'Anonymous'
    },
    urls: {
      create:  '/annotations_edit',
      read:    '/annotations_view/:id',
      update:  '/annotations_edit/:id',
      destroy: '/annotations_edit/:id',
      search:  '/annotations_search'
    }
  };

  if(options){
    jQuery.extend(self.settings, options);
  }

  self.initialize();
};

EEA.Annotator.prototype = {
  initialize: function(){
    var self = this;
    self.button = self.context.find('.annotator-button');
    self.button.attr('title', self.button.data('hide'));
    self.enabled = true;

    self.button.click(function(evt){
      evt.preventDefault();
      return self.click();
    });

    self.reload();
  },

  click: function(){
    var self = this;
    if(self.enabled){
      self.enabled = false;
      self.button.addClass('annotator-disabled');
      self.button.attr('title', self.button.data('show'));
      self.target.annotator('destroy');
    }else{
      self.enabled = true;
      self.button.removeClass('annotator-disabled');
      self.button.attr('title', self.button.data('hide'));
      self.reload();
    }
  },

  reload: function(){
    var self = this;

    // Init annotator
    self.target.annotator({
      readOnly: Boolean(self.settings.readOnly),
      exactMatch: true
    });

    // Permissions plugin
    self.target.annotator('addPlugin', 'Permissions', {
      user: self.settings.user,
      userId: function(user){
        if(user && user.id){
          return user.id;
        }
        return user;
      },
      userString: function(user){
        return EEA.AnnotatorUtil.userString(user);
      },
      showViewPermissionsCheckbox: false,
      showEditPermissionsCheckbox: false
    });

    // // Reply plugin
    self.target.annotator('addPlugin', 'Comment');

    // Storage plugin
    self.target.annotator('addPlugin', 'Store', {
      prefix: self.settings.prefix,
      urls: self.settings.urls
    });

  }
};


jQuery.fn.EEAAnnotator = function(options){
  return this.each(function(){
    var context = jQuery(this);
    var adapter = new EEA.Annotator(context, options);
    context.data('EEAAnnotator', adapter);
  });
};


/*
 **
 ** EEA Annotator Portlet
 **
 */
EEA.AnnotatorPortlet = function(context, options){
  var self = this;
  self.context = context;
  self.settings = {

  };

  if(options){
    jQuery.extend(self.settings, options);
  }

  self.initialize();
};

EEA.AnnotatorPortlet.prototype = {
  initialize: function(){
    var self = this;
    self.viewerHideTimer = null;

    self.viewer = new Annotator.Viewer({
      readOnly: true
    });

    self.viewer.hide().element.appendTo(self.context);

    self.viewer.element.bind({
      mouseover: function(evt){
        return self.clearViewerHideTimer(evt);
      },
      mouseout: function(evt){
        return self.startViewerHideTimer(evt);
      }
    });

    // Add comment text field
    self.viewer.addField({
      load: function(field, annotation){
        $(field).html(Util.escape(annotation.text));
      }
    });

    // Add comment user field
    self.viewer.addField({
      load: function(field, annotation){
        var userString = EEA.AnnotatorUtil.userString(annotation.user);
        $(field).html(userString).addClass('annotator-user');
      }
    });

    // Add replies field
    self.viewer.addField({
      load: function(field, annotation){
        var replies = annotation.replies;
        if(!replies || !replies.length){
          return;
        }

        var html = [
          "<div style='padding:5px' class='annotator-replies-header'> <span> Replies </span></div>",
          '<div id="Replies"><li class="Replies"></li></div>'
        ].join('\n');
        html = $(html);

        var where = html.find('.Replies');
        jQuery.each(replies, function(idx, reply){
          var div = [
            '<div class="reply">',
              '<div class="replytext">', reply.reply, '</div>',
              '<div class="annotator-user replyuser">', EEA.AnnotatorUtil.userString(reply.user), '</div>',
            '</div>'
          ].join('\n');
          $(div).appendTo(where);
        });

        html.appendTo($(field));
      }
    });

    self.reload(true);
  },

  reload: function(init){
    var self = this;
    var comments = self.context.find('.eea-annotator-comment');
    comments.each(function(){
      $(this)
        .mouseover(function(evt){
          self.clearViewerHideTimer();
          var viewerComment = $(this);

          var data = viewerComment.data('comment');
          var location = Util.mousePosition(evt, this);
          self.viewer.element.css(location);
          self.viewer.load([data]);

        })
        .mouseout(function(evt){
          return self.startViewerHideTimer();
        });
    });
  },

  clearViewerHideTimer: function(){
    clearTimeout(this.viewerHideTimer);
    this.viewerHideTimer = false;
  },

  startViewerHideTimer: function(){
    if (!this.viewerHideTimer) {
      this.viewerHideTimer = setTimeout(this.viewer.hide, 250);
    }
  }

};

jQuery.fn.EEAAnnotatorPortlet = function(options){
  return this.each(function(){
    var context = jQuery(this);
    var adapter = new EEA.AnnotatorPortlet(context, options);
    context.data('EEAAnnotatorPortlet', adapter);
  });
};


jQuery(document).ready(function(){

  // Annotator
  var items = jQuery(".eea-annotator");
  if(items.length){
    var userid = items.data('userid') || 'anonymous';
    var username = items.data('username') || userid;
    var settings = {
      prefix: jQuery('base').attr('href') + '/annotator.api',
      user: {
        id: userid,
        name: username
      }
    };

    items.EEAAnnotator(settings);
  }

  // Annotator Portlet
  items = jQuery(".eea-annotator-portlet");
  if(items.length){
    items.EEAAnnotatorPortlet();
  }

});
