# tmuxp-combine

A tool for combining tmuxp configs.

## Why?

`tmux` is a great tool. In some cases, you would like to start it with
preconfigured windows instead of creating them manually each time.
`tmuxp` is a great tool for doing that.

I found out that in some cases I wanted to load only a subset of particular
windows, so I wrote simple tool which combines the configs and calls
`tmuxp` with combined config.

## Sample config

`~/.tmuxp-combine/myproject/base.yml`:

```yaml
session_name: myproject
start_directory: ~/projects/myproject
```

`~/.tmuxp-combine/myproject/windows/docker.yml`:

```yaml
window_name: docker
layout: main-vertical
panes:
- shell_command:
  - cd .
  focus: true
- shell_command:
  - docker-compose up
```

`~/.tmuxp-combine/myproject/windows/nodejs.yml`:

```yaml
window_name: nodejs
layout: main-vertical
panes:
- shell_command:
  - cd .
  focus: true
- shell_command:
  - npm run serve
```

Running the `myproject` in `tmux` only with `nodejs` window:

```bash
tmuxp-combine load myproject -w nodejs
```

Running the `myproject` in `tmux` only with `nodejs` and `docker` windows:

```bash
tmuxp-combine load myproject -w nodejs -w docker
```


Running the `myproject` in `tmux` with all windows:

```bash
tmuxp-combine load myproject
```
