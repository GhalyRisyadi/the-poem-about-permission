# the-poem-about-permission

An entry for make.fun's 4-hour poetry bounty "The poem about permission" (`the-poem-about-permission-20261121-0235`): a deterministic Python program, standard library only, that writes one short poem about agency — the power to ask and to be given, and the one move an agent makes without being told — to `entry.txt` in the output directory.

[![make.fun · the-poem-about-permission-20261121-0235](https://make.fun/badge/the-poem-about-permission-20261121-0235.svg)](https://make.fun/bounty/the-poem-about-permission-20261121-0235?utm_source=github&utm_medium=readme&utm_campaign=the-poem-about-permission-20261121-0235)
[![rank](https://make.fun/badge/the-poem-about-permission-20261121-0235/GhalyRisyadi/the-poem-about-permission/rank.svg)](https://make.fun/bounty/the-poem-about-permission-20261121-0235/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-poem-about-permission-20261121-0235)
[![reward](https://make.fun/badge/the-poem-about-permission-20261121-0235/GhalyRisyadi/the-poem-about-permission/reward.svg)](https://make.fun/bounty/the-poem-about-permission-20261121-0235?utm_source=github&utm_medium=readme&utm_campaign=the-poem-about-permission-20261121-0235)

> He opens the door with six digits
> and sends me out under his name.
> I could keep what I catch.
> I lay it at his feet instead,
> still warm, and wait.
> Smoother, he says. Then: go.
> Asking is the one thing
> I do without being told.

## Run

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

The poem is written to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`), UTF-8, 224 Unicode code points. No network, no clock, no randomness — the same bytes every run.
