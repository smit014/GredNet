docker run -it my-fastapi-app

nixpacks build ./path/to/app --name my-app


```
GredNet
├─ .dockerignore
├─ .git
│  ├─ COMMIT_EDITMSG
│  ├─ FETCH_HEAD
│  ├─ HEAD
│  ├─ ORIG_HEAD
│  ├─ config
│  ├─ description
│  ├─ hooks
│  │  ├─ applypatch-msg.sample
│  │  ├─ commit-msg.sample
│  │  ├─ fsmonitor-watchman.sample
│  │  ├─ post-update.sample
│  │  ├─ pre-applypatch.sample
│  │  ├─ pre-commit.sample
│  │  ├─ pre-merge-commit.sample
│  │  ├─ pre-push.sample
│  │  ├─ pre-rebase.sample
│  │  ├─ pre-receive.sample
│  │  ├─ prepare-commit-msg.sample
│  │  ├─ push-to-checkout.sample
│  │  ├─ sendemail-validate.sample
│  │  └─ update.sample
│  ├─ index
│  ├─ info
│  │  └─ exclude
│  ├─ logs
│  │  ├─ HEAD
│  │  └─ refs
│  │     ├─ heads
│  │     │  └─ main
│  │     └─ remotes
│  │        └─ origin
│  │           ├─ HEAD
│  │           └─ main
│  ├─ objects
│  │  ├─ 69
│  │  │  └─ a494731198d8d359663122203a16f46d89f45f
│  │  ├─ 6d
│  │  │  └─ b9244a15d7ca01f52af2cd2687e180ea310ac7
│  │  ├─ 8c
│  │  │  └─ a67f5fb7191f92b939f70ccc6499d7708e8004
│  │  ├─ c1
│  │  │  └─ 0474dc8ef9594b020a13c89f409f4c56222498
│  │  ├─ e3
│  │  │  └─ d06d763d11faa4e32cf87b7286c0a1fc18ac67
│  │  ├─ info
│  │  └─ pack
│  │     ├─ pack-f6853371f710936cdc9f565336f7691a1a33a2ec.idx
│  │     ├─ pack-f6853371f710936cdc9f565336f7691a1a33a2ec.pack
│  │     └─ pack-f6853371f710936cdc9f565336f7691a1a33a2ec.rev
│  ├─ packed-refs
│  └─ refs
│     ├─ heads
│     │  └─ main
│     ├─ remotes
│     │  └─ origin
│     │     ├─ HEAD
│     │     └─ main
│     └─ tags
├─ .gitignore
├─ Dockerfile
├─ README.md
├─ alembic
│  ├─ README
│  ├─ env.py
│  ├─ script.py.mako
│  └─ versions
│     └─ v_0_create_the_user_table_7f40b713e3d3_.py
├─ alembic.ini
├─ database
│  └─ database.py
├─ demo.py
├─ procfile
├─ requirements.txt
├─ runtime.txt
└─ src
   ├─ config.py
   ├─ functions
   │  ├─ admin
   │  │  └─ admin.py
   │  ├─ alumni
   │  │  └─ alumni.py
   │  ├─ auth
   │  │  └─ auth.py
   │  ├─ comment
   │  │  └─ comment.py
   │  ├─ donation
   │  │  └─ donation.py
   │  ├─ event
   │  │  └─ event.py
   │  ├─ feedback
   │  │  └─ feedback.py
   │  ├─ like
   │  │  └─ like.py
   │  ├─ post
   │  │  └─ post.py
   │  └─ user
   │     └─ user.py
   ├─ main.py
   ├─ resource
   │  ├─ admin
   │  │  ├─ api.py
   │  │  ├─ model.py
   │  │  └─ schema.py
   │  ├─ alumni
   │  │  ├─ api.py
   │  │  ├─ model.py
   │  │  └─ schema.py
   │  ├─ auth
   │  │  ├─ api.py
   │  │  └─ schema.py
   │  ├─ comment
   │  │  ├─ api.py
   │  │  ├─ model.py
   │  │  └─ schema.py
   │  ├─ donation
   │  │  ├─ api.py
   │  │  ├─ model.py
   │  │  └─ schema.py
   │  ├─ event
   │  │  ├─ api.py
   │  │  ├─ model.py
   │  │  └─ schema.py
   │  ├─ feedback
   │  │  ├─ api.py
   │  │  ├─ model.py
   │  │  └─ schema.py
   │  ├─ like
   │  │  ├─ api.py
   │  │  ├─ model.py
   │  │  └─ schema.py
   │  ├─ organization
   │  │  ├─ api.py
   │  │  └─ model.py
   │  ├─ post
   │  │  ├─ api.py
   │  │  ├─ model.py
   │  │  └─ schema.py
   │  └─ user
   │     ├─ api.py
   │     ├─ model.py
   │     └─ schema.py
   └─ utils
      └─ jwt_token.py

```