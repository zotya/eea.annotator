#  EEA Annotator

[![http://ci.eionet.europa.eu/job/eea.annotator-
www/badge/icon](https://camo.githubusercontent.com/01195f7e232850b54c266277f3ff7f334549b8e8/687474703a2f2f63692e65696f6e65742e6575726f70612e65752f6a6f622f6565612e616e6e6f7461746f722d7777772f62616467652f69636f6e)](http://ci.eionet.europa.eu/job/eea
.annotator-www/lastBuild) [![http://ci.eionet.europa.eu/job/eea.annotator-
plone4/badge/icon](https://camo.githubusercontent.com/42a487ed303e8c93a0a967537c49efe0439f4f28/687474703a2f2f63692e65696f6e65742e6575726f70612e65752f6a6f622f6565612e616e6e6f7461746f722d706c6f6e65342f62616467652f69636f6e)](http://ci.eionet.europa.eu/job/eea
.annotator-plone4/lastBuild)

EEA Annotator is the Plone integration of <http://okfnlabs.org/annotator/>
which allows your editors to easily collaborate on a Plone document by adding
annotations (inline comments) on it.

[![http://eea.github.io/_images/eea.annotator.cover.png](https://camo.githubusercontent.com/b933349c8f1f298d686ad13d2e1108e567fd7b60/687474703a2f2f6565612e6769746875622e696f2f5f696d616765732f6565612e616e6e6f7461746f722e636f7665722e706e67)](http://www.youtube.com/watch?v=UExygLRqjkc&list=PLVPSQz7ahsBxXe_sM7Cx2BnOoxkt3pnbw&feature=share)

##  Contents

Contents

  * Contents
  * Main features
  * Install
  * Getting started
  * Moderate inline comments
    * Dexterity
  * Source code
  * Copyright and license
  * Funding

##  Main features

  1. Inline comments on any webpage.
  2. Portal types aware. Possibility to enable inline comments only for certain content types.
  3. Workflow aware. Possibility to enable/disable inline comments only for certain workflow states (via content rules).
  4. Events. Possibility to define custom content-rules based on inline comments events: add/reply/close/re-open/delete (e.g. notify users by e-mail)
  5. Dexterity aware. It works also with dexterity content-types.
  6. Contextually disable inline comments.
  7. Moderate inline comments.

##  Install

  * Add eea.annotator to your eggs section in your buildout and re-run buildout. You can download a sample buildout from <https://github.com/eea/eea.annotator/tree/master/buildouts/plone4>
  * Install eea.annotator within Site Setup &gt; Add-ons

Warning

Once you'll install this add-on via Site Setup &gt; Add-ons, it will overrides
Publish Traversal for Archetypes base object
(plone.app.imaging.interfaces.IBaseObject) and Dexterity Base Content
(plone.dexterity.interfaces.IDexterityContent) in order to handle custom
annotator URLs. Still, it preserves old functionality from plone.app.imaging
and plone.dexterity (also eea.depiction) but if you have custom traversals
registered for these interfaces, try to use custom browser layers when
registering them (see: eea.annotator.browser.app.traverse).

**Plone version dependency**

eea.annotator does not have a hard dependency on Plone 4.3, however, it has
been built around plone.app.jquery version 1.7.2 which is shipped by default
with Plone 4.3. If you wish to use the product on an older version of Plone,
you could pin the plone.app.jquery version to 1.7.2.

##  Getting started

  1. Go to Plone Site Setup &gt; EEA Annotator Settings and enable inline comments for your content-types (default enabled for Page).
  2. Go to your work-space within Plone Site and add a new object (Page) or user an existing one.
  3. In view mode select text you want to comment on and add an inline comment.
  4. Within edit form &gt; Settings Tab you can contextually disable inline comments.
  5. You can also add an "Inline comments" portlet in order to overview all inline comments on this page.

##  Moderate inline comments

Warning

You'll have to be logged-in ad Manager or have the **eea.annotator: Manage**
permission

  1. Click on the title of the **Inline comments portlet** if any or just access **@@moderate-inline-comments**

###  Dexterity

Dexterity content-types are supported by EEA Annotator.

  1. In order to be able to contextually disable inline comments you need to add a boolean field called disableAnnotator within your Dexterity content-type schema fields.
  2. In order to be able to contextually make inline comments read-only you need to add a boolean field called readOnlyAnnotator within your Dexterity content-type schema fields. (Plone Site Setup &gt; Dexterity Content Types &gt; MyCustomType &gt; Fields)

##  Source code

  * Latest source code (Plone 4 compatible): <https://github.com/collective/eea.annotator>

##  Copyright and license

The Initial Owner of the Original Code is European Environment Agency (EEA).
All Rights Reserved.

The EEA Annotator (the Original Code) is free software; you can redistribute
it and/or modify it under the terms of the GNU General Public License as
published by the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

More details under docs/License.txt

##  Funding

[EEA](http://www.eea.europa.eu/) \- European Environment Agency (EU)

