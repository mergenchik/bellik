---
title: GitHub Setup
intro: Small manual to start your repository on GitHub for your project.
versions:
  fpt: '*'
  ghes: '*'
  ghae: '*'
  ghec: '*'
---

First we create a repository in GitHub. If you do not have account please create one.

{% tip %}

As a developer, it is recommended to have GitHub account, so that you can contribute some code to community. Also, some companies prefer developers who have GitHub account and contribute to open source.

Please select your github username vicely. Also, it will be very good if you have the same email as your github username.

Selecting avatar is also preferred. Treat your github profile as your CV.

{% endtip %}

## Note on GitHub account


## Repository setup

You can go to your github account, and press a plus sign on right top, near your profile picture or directly go to [https://github.com/new](https://github.com/new).

![new repository screen](images/github_setup/01_create_repository.png)

Provide repository name, select if it is private or public. If you want there are ready templates for .gitignore files, select accoridng your project. Also, if you are developing open source project, you can select from existing licenses.

After repository created, you will have screen as below.

![repository just created screen](images/github_setup/02_repository_created.png)

You can clone that repository to your local machine to start developing.

For this project command to clone repository is

```
git clone git@github.com:mergenchik/bellik.git
```

please note that, you should have your SSH keys setup in your github profile.

## Wiki Setup

The most important part of any software is documentation. Keeping documentation up to date is very difficult task.

GitHub provides Wiki pages, a separate repository, where you can store documentation and manage it parallel to source code.

In your repository click Wiki tab and you will see Wiki Section as on screen below.

![empty wiki section](images/github_setup/03_wiki_section.png)

Click on "create first page" and you will have screen as below.

![new wiki page](images/github_setup/04_new_wiki_page.png)

You can clone Wiki repository (please clone to separate location, not inside your other repository) with belo command.

```
git clone git@github.com:mergenchik/bellik.wiki.git
```
