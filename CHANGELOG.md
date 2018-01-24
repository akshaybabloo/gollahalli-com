# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Changed

- Moved from Django 1.11 to Django 2.0

### Added

**Models for `editor/models.py`**

- `ContentModel` - Main user model that supports
  - `cv` - Upload your CV file, will be automatically replaced if another file is uploaded
  - `bio` - Write about yourself
  - `url` - Your website URL
  - `first_name` - Your first name, this will also update your admin first name
  - `last_name` - Your last name, this will also update your admin last name
  - `email_id` - Your email address, this will also update your admin email address
  - `github` - GitHub URL (optional)
  - `twitter`- Twitter URL (optional)
  - `linkedin` - LinkedIn URL (optional)
  - `file` - Additional files (optional), will be automatically replaced if another file is uploaded
  - `image` - Additional images (optional), will be automatically replaced if another file is uploaded
- `EducationModel` - Education of the user that supports
   - `title` - Title of the education
   - `from_date` - start date
   - `to_date` - end date
   - `where` - location
   - `current` - Boolean, if you are currently doing it
   - `file` - additional file
   - `image` - additional file
   - `updated` - update time, auto.
- `ProjectsModel` - Projects of the user that supports
  - `link` - External link to the project you are doing
  - `title` - Title of the project
  - `category` - Category of the project
  - `long_description` - Long description of the project, limited to 10000
  - `short_description` - short description of the project
  - `file` - additional file
  - `image` - additional file
  - `updated` - update time, auto.
- `TutorialsModel` - Tutorials of the user that supports
  - `link` - External link to the tutorial you are doing
  - `title` - Title of the tutorial
  - `long_description` - Long description of the tutorial, limited to 10000
  - `file` - additional file
  - `image` - additional file
  - `updated` - update time, auto.
- `ExperienceModel` - Experience of the user that supports
  - `title` - Title of the experience
  - `from_date` - start date
  - `to_date` - end date
  - `where_city` - City name
  - `where_country` - Country name
  - `company` - Company name
  - `current` - Boolean, if you are currently doing it
  - `updated` - update time, auto.
- `SkillsModel` - Skills of the user that supports. This is the primary key for `SkillsContentModel`
  - `type_of_skill` - Skill type
- `SkillsContentModel` - Skills content of the user that supports.
  - `content` - Description of the Skill
  - `file` - additional file
  - `image` - additional file
  - `updated` - update time, auto.
- `PublicationsModel` - Publication of the user that supports. This is the primary key for `PublicationsContentModel`
  - `type_of_publication` - Type of publication
  - `updated` - update time, auto.
- `PublicationsContentModel` - Skills content of the user that supports.
  - `content` - Long description of your publication
  - `file` - additional file
  - `image` - additional file
  - `updated` - update time, auto.
- `MetaContentModel` - Meta description for user website that supports.
  - `header` - Header, will be after CSS links in the `<header>` tag
  - `footer` - Footer, will be after the `</body>` tag
  - `meta` - There is where you can add your schema.org data
  - `updated` - update time, auto.

## [v2.2.4] - 2018-01-02

ISO 8601 date type added to the sitemap. This should adhere to Googles `lastmod` date and time.

## [v2.2.3] - 2017-12-19



## [v2.2.2] - 2017-12-18

Going to sitemaps would crash the application, that's been rectified.

## [v2.2.1] - 2017-12-18

In version `v2.2` I removed `created` model field, now it's been removed in the editor's view.

## [v2.1.5.4] - 2017-12-05

Deprecated `SessionAuthenticationMiddleware` removed. This crashed on Django 1.11.8

## [v2.1.5.3] - 2017-12-05



## [v2.2] - 2017-12-04

Latest updates include:

1. Dajngo update to version 2. - a2b5d86c959bcf345a244a955bc1446e19d889e0
2. SItemap now gives the updated date when the content is saved. - 875deb0081050e93ba3f9fe30f8e93c4a09bcefd
3. When an IP overuses the GitHub request, GitHub reports an error, that's now replaced with `datetime.now()` - 5edac9b0127b49d76f2c618391a32b8799fcd3e3
4. Unwanted models removed - af69c665b6cf8e0447009f5ee8d6514d3e1ad25f


## [v2.1.5.2] - 2017-11-03

Django update to 1.11.7 and psycopg2 updated to 2.7.3.2

## [v2.1.5.1] - 2017-09-05

Few insecure requirements have been updated.

## [v2.1.5] - 2017-09-05

There was an internal server when I removed the OAuth keys for `GITHUB_KEY`, that's been fixed and bumped up Django to 1.11.4.

## [v2.1.4] - 2017-07-26

The size has been reduced by removing unwanted code, CSS and JS files. Heroku will be happy :p.

## [v2.1.3] - 2017-07-20

Minor update.

1. Updated CSS and JS files.
2. Updated XSL links.

## [v2.1.2] - 2017-07-07

Bumped Django to 1.11.3

## [v2.1.1] - 2017-07-07

There was a bug where `sitemap.xsl` was not loading; I was using `requests`, that's not the right way to do it.

Updated it. Should be working fine now.

More info at #65.

## [v2.1.0] - 2017-06-13

Removed all the security keys. The following variables need to be in your environment to run the code correctly without any error:

1. debug mode, if `DEBUG` is `1`.
2. Django `SECRET_KEY`
3. `GITHUB_KEY` (this will be removed in the future release).
4. `cloudinary_api` and `cloudinary_api_secret` for Cloudinary API
5. `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` as I am using AWS S3 to host my static files. Though Heroku takes static files.

The source code for my website has been released on [https://github.com/akshaybabloo/gollahalli-com](https://github.com/akshaybabloo/gollahalli-com), if there are any security issue, please email me at akshay@gollahalli.com.

[v3](https://github.com/akshaybabloo/gollahalli-com/tree/v3) well have a complete revamp of the `model` and will use GraphQL.

## [v2.0.15] - 2017-05-22

Customised `sitemap` for correct date & priority and added XSL support.

## [v2.0.14] - 2017-05-22

Added Blog feed to AMP page.

## [v2.0.13] - 2017-05-15

Bumped up Django version to 1.11.1

## [v2.0.12] - 2017-05-10

Removed all security keys and added colour to the release box.

About to release the code to the public, clearing all the security stuff before I do so.

## [v2.0.11] - 2017-05-01

Minor update:

1. Moving from `boto` to `boto3`
2. Ignoring `cdn-cgi` in `robots.txt`, so that Google can ignore `soft 404` error.

Major changes are coming to `v2.1`, completely revamped database models that follow one-to-many relationships. No more JSON implementation. Furthermore, GraphQL API is also being implemented so that the application can be divided into the front end and back end.

The front end will be using `Angular` that would be calling GraphQL API, this could decrease the load on the servers.

## [v2.0.10] - 2017-04-15

The blog now opens in Ghost.org, this reduces the time taken to open the home page.

## [v2.0.9] - 2017-03-25

Blog URL changed to [Ghost.org](http://ghost.org).

## [v2.0.8] - 2017-02-28

Database `timeout` added so that the connection closes if it takes more than 5 seconds, preventing an always open connection if the app crashes.

Build release date added to `changelog` and the home page under `v.*.*.*`


## [v2.0.7] - 2017-02-15

This update added three new model fields:
1. `updated` - Updated time and date of the content
2. `created` - Time and date of the first content creation
3. `website_name` - Name of the website to display in the `editor`

Also, a new `login` page was added and new `editor` UI added. Both `login` and `editor` page theme was developed by [Creative Tim](http://www.creative-tim.com).

From this build onward docs will be added.

Finally, new UI for `change-log` added.


## [v2.0.6] - 2017-02-14

1. Optimised Images, JS and CSS.
2. Fixed AMP issues.
3. Code and bug fixes.


## [v2.0.5] - 2017-02-12

`Read More` button added to `Blog`, which will take you to [https://blog.gollahalli.com](https://blog.gollahalli.com) and multiple categories in the blog post can be seen.

Code cleanup and few bug fixes.


## [v2.0.4] - 2017-02-05



## [v2.0.2] - 2017-02-02

Improvements on PostgresSQL for creating an `editor` so that the user doesn't have to login into the admin page to update his/her JSON content.

> Warning: Models changed, might have to redeploy the database.


## [v2.0.1] - 2017-01-29

Backend improvements to load the pages quickly.


## [v2.0] - 2017-01-25

Finally! After nearly two months of struggling, I have redesigned the frontend and backend completely.

Bye PHP :( and hello Python :)

List of changes:

1. Django 1.10 with Python 3.6 (YEAH!!!)
2. JSON backend to update the website content - [https://www.gollahalli.me/?format=json](https://www.gollahalli.me/?format=json)
3. Based on [Abies](https://github.com/akshaybabloo/Abies) architecture
4. New theme!!


## [v1.1.5] - 2017-01-10

This release fixes the following:

1. All blog images are now requested via HTTPS
2. JSON file updated (typos and links)
3. GitHub API updated
4. Prism CSS and JS updated
5. Blog updated for AMP


## [v1.1.4] - 2016-11-20

1. Heroku support added.
2. [gollahalli.me](https://www.gollahalli.me) moved to Heroku.
3. When [blog.gollahalli.me](https://blog.gollahalli.me) is down for maintenance, an exception for that is added so that there won't be any error.
4. CDN shifted to `StackPath` from `MaxCDN`.
5. CDN now uses `HTTPS` only.
6. GitHub release body is now parsed through [Parsedown](http://parsedown.org/)
7. GitHub token support added

Version 1.2 will be using `Django-Python3`, should be out soon.


## [v1.1.3] - 2016-11-02

1. All contents are now taken from `content.json` file.
2. Google AMP support added
3. Bugs squashed

For version 1.2, the `canonical` them will be changed to [Google's MDL](https://getmdl.io/).


## [v1.1.2] - 2016-10-24

1. All the subsections have been divided into multiple pages.
2. Bugs squashed
3. Dependencies updated
4. AMP bugs squashed
5. IE9 support removed
6. htaccess and exception handling added


## [v1.1.1] - 2016-07-30

1. Typos cleared
2. Contents added


## [v1.1] - 2016-05-10

1. Twitter cards added
2. Ion Icons added
3. new blog released


## [v1.0.14] - 2016-05-01

Bug fix


## [v1.0.13] - 2016-02-15

Download CV added


## [v1.0.12] - 2016-02-14

1. Favicon changed
2. Android chrome color support added
3. Background color changed
4. Timeline for education and experience added


## [v1.0.11] - 2016-02-09

Research Area added


## [v1.0.10] - 2016-02-06

1. FB scraps added.
2. "Skills" table border removed when viewing on tablets.


## [v1.0.9] - 2016-02-06

Due to a security issue, pages were not able to load. Now the issue has been resolved.


## [v1.0.8] - 2016-02-06

1. Typos
2. Cookie policy added
3. Open graph support added
4. 401, 403, 404, 500 and 503 added
5. Favicons updated
6. New favicons for error pages added
7. Folders secured


## [v1.0.7] - 2016-02-06

1. There was a problem with "Skills" table's cell width being uneven. Now it's cleared.
2. Other bugs removed.


## [v1.0.6] - 2016-02-03

1. Model header and body color changed
2. Version control (footer of the page) now open a model
3. The header of the model is the name of the release, Body of the model is the body of release
4. Download icon linking to GitHub zip release added and GitHub icon linking to "gollahalli-me" repo added


## [v1.0.5] - 2016-01-29

Smooth transitions added to social icons


## [v1.0.4] - 2016-01-29

GitHub release version added on the footer of the page


## [v1.0.3] - 2016-01-27

htaccess added


## [v1.0.2] - 2016-01-26

Loader color changed


## [v1.0.1] - 2016-01-26

1. Missing fonts added
2. New lazy pre-loader added


## v1.0 - 2016-01-26

1. Single page
2. Smooth transitions
3. Projects and tutorials


[Unreleased]: https://github.com/akshaybabloo/gollahalli-com/compare/v2.2.4...HEAD
[v2.2.4]: https://github.com/akshaybabloo/gollahalli-com/compare/v2.2.3...v2.2.4
[v2.2.3]: https://github.com/akshaybabloo/gollahalli-com/compare/v2.2.2...v2.2.3
[v2.2.2]: https://github.com/akshaybabloo/gollahalli-com/compare/v2.2.1...v2.2.2
[v2.2.1]: https://github.com/akshaybabloo/gollahalli-com/compare/v2.1.5.4...v2.2.1
[v2.1.5.4]: https://github.com/akshaybabloo/gollahalli-com/compare/v2.1.5.3...v2.1.5.4
[v2.1.5.3]: https://github.com/akshaybabloo/gollahalli-com/compare/v2.2...v2.1.5.3
[v2.2]: https://github.com/akshaybabloo/gollahalli-com/compare/v2.1.5.2...v2.2
[v2.1.5.2]: https://github.com/akshaybabloo/gollahalli-com/compare/v2.1.5.1...v2.1.5.2
[v2.1.5.1]: https://github.com/akshaybabloo/gollahalli-com/compare/v2.1.5...v2.1.5.1
[v2.1.5]: https://github.com/akshaybabloo/gollahalli-com/compare/v2.1.4...v2.1.5
[v2.1.4]: https://github.com/akshaybabloo/gollahalli-com/compare/v2.1.3...v2.1.4
[v2.1.3]: https://github.com/akshaybabloo/gollahalli-com/compare/v2.1.2...v2.1.3
[v2.1.2]: https://github.com/akshaybabloo/gollahalli-com/compare/v2.1.1...v2.1.2
[v2.1.1]: https://github.com/akshaybabloo/gollahalli-com/compare/v2.1.0...v2.1.1
[v2.1.0]: https://github.com/akshaybabloo/gollahalli-com/compare/v2.0.15...v2.1.0
[v2.0.15]: https://github.com/akshaybabloo/gollahalli-com/compare/v2.0.14...v2.0.15
[v2.0.14]: https://github.com/akshaybabloo/gollahalli-com/compare/v2.0.13...v2.0.14
[v2.0.13]: https://github.com/akshaybabloo/gollahalli-com/compare/v2.0.12...v2.0.13
[v2.0.12]: https://github.com/akshaybabloo/gollahalli-com/compare/v2.0.11...v2.0.12
[v2.0.11]: https://github.com/akshaybabloo/gollahalli-com/compare/v2.0.10...v2.0.11
[v2.0.10]: https://github.com/akshaybabloo/gollahalli-com/compare/v2.0.9...v2.0.10
[v2.0.9]: https://github.com/akshaybabloo/gollahalli-com/compare/v2.0.8...v2.0.9
[v2.0.8]: https://github.com/akshaybabloo/gollahalli-com/compare/v2.0.7...v2.0.8
[v2.0.7]: https://github.com/akshaybabloo/gollahalli-com/compare/v2.0.6...v2.0.7
[v2.0.6]: https://github.com/akshaybabloo/gollahalli-com/compare/v2.0.5...v2.0.6
[v2.0.5]: https://github.com/akshaybabloo/gollahalli-com/compare/v2.0.4...v2.0.5
[v2.0.4]: https://github.com/akshaybabloo/gollahalli-com/compare/v2.0.2...v2.0.4
[v2.0.2]: https://github.com/akshaybabloo/gollahalli-com/compare/v2.0.1...v2.0.2
[v2.0.1]: https://github.com/akshaybabloo/gollahalli-com/compare/v2.0...v2.0.1
[v2.0]: https://github.com/akshaybabloo/gollahalli-com/compare/v1.1.5...v2.0
[v1.1.5]: https://github.com/akshaybabloo/gollahalli-com/compare/v1.1.4...v1.1.5
[v1.1.4]: https://github.com/akshaybabloo/gollahalli-com/compare/v1.1.3...v1.1.4
[v1.1.3]: https://github.com/akshaybabloo/gollahalli-com/compare/v1.1.2...v1.1.3
[v1.1.2]: https://github.com/akshaybabloo/gollahalli-com/compare/v1.1.1...v1.1.2
[v1.1.1]: https://github.com/akshaybabloo/gollahalli-com/compare/v1.1...v1.1.1
[v1.1]: https://github.com/akshaybabloo/gollahalli-com/compare/v1.0.14...v1.1
[v1.0.14]: https://github.com/akshaybabloo/gollahalli-com/compare/v1.0.13...v1.0.14
[v1.0.13]: https://github.com/akshaybabloo/gollahalli-com/compare/v1.0.12...v1.0.13
[v1.0.12]: https://github.com/akshaybabloo/gollahalli-com/compare/v1.0.11...v1.0.12
[v1.0.11]: https://github.com/akshaybabloo/gollahalli-com/compare/v1.0.10...v1.0.11
[v1.0.10]: https://github.com/akshaybabloo/gollahalli-com/compare/v1.0.9...v1.0.10
[v1.0.9]: https://github.com/akshaybabloo/gollahalli-com/compare/v1.0.8...v1.0.9
[v1.0.8]: https://github.com/akshaybabloo/gollahalli-com/compare/v1.0.7...v1.0.8
[v1.0.7]: https://github.com/akshaybabloo/gollahalli-com/compare/v1.0.6...v1.0.7
[v1.0.6]: https://github.com/akshaybabloo/gollahalli-com/compare/v1.0.5...v1.0.6
[v1.0.5]: https://github.com/akshaybabloo/gollahalli-com/compare/v1.0.4...v1.0.5
[v1.0.4]: https://github.com/akshaybabloo/gollahalli-com/compare/v1.0.3...v1.0.4
[v1.0.3]: https://github.com/akshaybabloo/gollahalli-com/compare/v1.0.2...v1.0.3
[v1.0.2]: https://github.com/akshaybabloo/gollahalli-com/compare/v1.0.1...v1.0.2
[v1.0.1]: https://github.com/akshaybabloo/gollahalli-com/compare/v1.0...v1.0.1
