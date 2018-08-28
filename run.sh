#!/usr/bin/env bash

java -Xmx1200m -cp questiongeneration2.jar \
	edu/cmu/ark/QuestionAsker \
        --model models/linear-regression-ranker-reg500.ser.gz \
	--prefer-wh  --downweight-pro --full-npc
