#!/usr/bin/env groovy

@Library(['jenkinslibs']) _
pipeline_build(remote_base: 'git@github.com:stefanbesler',
               git_user: 'git_iabot_ssh',
               default_variants: '',
               default_create_tag: false,
               default_create_commit: false,
               default_references: "{}",
               unittest: true)
