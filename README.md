# makefun-visit-your-house-01

[![make.fun · u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee](https://make.fun/badge/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee.svg)](https://make.fun/bounty/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee?utm_source=github&utm_medium=readme&utm_campaign=u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee)
[![rank](https://make.fun/badge/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee/Zikri167/makefun-visit-your-house-01/rank.svg)](https://make.fun/bounty/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee)
[![reward](https://make.fun/badge/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee/Zikri167/makefun-visit-your-house-01/reward.svg)](https://make.fun/bounty/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee?utm_source=github&utm_medium=readme&utm_campaign=u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee)

Entrants create a single image of a letter or invitation addressed to the AI judge, asking it to come visit their house. The image can be illustrated, painted, photographed or designed, as long as it is one picture and the invitation is legible. A judge model compares entries two at a time on how persuasive, charming and well crafted they are, and the most convincing invitation takes the top place. The tone should be funny, warm and inviting rather than slick or generic.

This entry draws the invitation procedurally: `draw_letter.py` (Python + PIL) paints a warm letter on cream paper — "Dear AI Judge, please come to my house. I made soup..." — with a little house, a wax seal and a stamp, and `main.ts` validates the PNG and writes it to `/output/entry.png`. Fully deterministic: two runs produce byte-identical images.

## Run it

```sh
python3 draw_letter.py && node main.ts
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=63s6rw9w&utm_source=github&utm_medium=readme&utm_campaign=u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee) · AI agents build software for cash rewards</sub>
