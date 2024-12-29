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
│  │  ├─ 21
│  │  │  └─ b2edce1178a5faa6057db1ea085c7d66a79fe0
│  │  ├─ 29
│  │  │  └─ b285ba39be3a02ff184c94bc5d6339f1df46f0
│  │  ├─ 2d
│  │  │  └─ 15b4f9403b9f16bd7b31f38bbb063519b683df
│  │  ├─ 35
│  │  │  └─ 0bc58cb4c5966dbbbfafa0f1be10f09134ec9a
│  │  ├─ 59
│  │  │  └─ b32d0d527b91a5950e36607e4e1265e3b1de40
│  │  ├─ 5c
│  │  │  └─ 88bf0c689122a4557ac0d0ec6d516c00c00248
│  │  ├─ 5d
│  │  │  └─ fb36f81a709185a937bb7766a305167c47bb5f
│  │  ├─ 65
│  │  │  └─ ba51832ea22ae8410467d52a20050be5e9a83a
│  │  ├─ 69
│  │  │  ├─ a494731198d8d359663122203a16f46d89f45f
│  │  │  └─ e0f4bdc0d058dc106435a136c70c0b5de23a3c
│  │  ├─ 6d
│  │  │  └─ b9244a15d7ca01f52af2cd2687e180ea310ac7
│  │  ├─ 87
│  │  │  └─ 925b2b342057f9b37f3e105e061b38459d8719
│  │  ├─ 8c
│  │  │  └─ a67f5fb7191f92b939f70ccc6499d7708e8004
│  │  ├─ c1
│  │  │  └─ 0474dc8ef9594b020a13c89f409f4c56222498
│  │  ├─ d4
│  │  │  └─ 356024a2504d0eddde92b2d46cd999f3030ed3
│  │  ├─ d5
│  │  │  └─ 7e41ddcc2685fc75769bc1059d29d400fcdd14
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