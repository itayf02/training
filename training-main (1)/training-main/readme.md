# AICOE Training

This is the AICOE official training repository. Welcome!

Before anything else, please read the magnificent [training manifest](training_manifest.pdf).
Hopefully it will help you find your own way through the training.

Some technical instructions before we start:
- Clone this repo to your local computer (or colab). This repo only contains code and notebook files, but not the datasets.
For downloading the datasets from [our drive](https://drive.google.com/drive/folders/1NDV1ZgBE3NWzPgv1A_Q0_xExr0jQecsU?usp=drive_link),
use [gdown](https://github.com/wkentaro/gdown#--gdown).
- You will use your own forked repo for solutions. Push your solutions before meeting with your tutor.
- Use a proper IDE such as PyCharm/DataSpell/VSCode for code and notebooks. Use google colab only if you have to (e.g. no GPU on localhost).
We can offer many GPU solutions - ask your tutor.
- Probably you'll find some typos/things that don't work/old stuff during training.
The training obviously contains some errors, and you are here to fix it.
Please open a new branch to fix these issues and open a pull request (branch format: `fix/description`).


## Resources
Some exercises have mandatory readings. You can find it here as well as additional material:
- [Recommended Resources](https://dazzling-player-a73.notion.site/Recommended-Resources-b648fd1482014394920b284c545b0f6c) (or [this link](https://github.com/AI-COE-git/training/blob/main/Recommended%20Resources.md))
- [Training Reading Material](https://dazzling-player-a73.notion.site/Training-Reading-Materials-7c4da2dd9b4c4237878f239103899de2) (or [this link](https://github.com/AI-COE-git/training/blob/main/Training%20Reading%20Materials.md))

## The Training Curriculum
The training has 3 fundamental parts, and some electives. The first part is a short intro course for machine learning.
The second part will focus on deep learning and more advanced concepts. In the last part you will encounter some experimental work.
You and your tutor are encouraged to change the original format, add elective exercises from here or from external courses,
add reading material etc. as long as you on time with the 3-month period plan.

### Introduction and Classic ML
| הערכת זמן בימים | טכני                | מחקרי              | אלגוריתמי          | תרגיל                                                                                                                                   |
|:---------------:|---------------------|--------------------|--------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
|        1        | :heavy_check_mark:  |                    |                    | [python](intro/python/python)                                                                                                           |
|        1        | :heavy_check_mark:  |                    |                    | [numpy](intro/python/numpy)                                                                                                             |
|       1.5       | :heavy_check_mark:  |                    |                    | [pandas](intro/python/pandas)                                                                                                           |
|       0.5       | :heavy_check_mark:  |                    |                    | [visualization](intro/python/visualization)                                                                                             |
|     0.5-1.5     |                     | :heavy_check_mark: | :heavy_check_mark: | ([regression recitation](intro/regression/recitation)) + [regression exercise](intro/regression/exercise)                               |
|       1-3       |                     | :heavy_check_mark: | :heavy_check_mark: | ([unsupervised recitation](intro/unsupervised/recitation)) + [unsupervised exercise](intro/unsupervised/exercise)                       |
|       1-3       |                     | :heavy_check_mark: | :heavy_check_mark: | ([supervised recitation](intro/supervised/recitation)) + [supervised exercise](intro/supervised/exercise)                               |
|       1.5       | :heavy_check_mark:  |                    | :heavy_check_mark: | [feature engineering exercise](intro/feature_engineering)                                                                               |
|        1        |                     | :heavy_check_mark: | :heavy_check_mark: | ([basic neural networks recitation](intro/nn_intro/part1/recitation)) + [basic neural networks exercise](intro/nn_intro/part1/exercise) |
|        1        |                     | :heavy_check_mark: | :heavy_check_mark: | [advanced neural networks](intro/nn_intro/part2)                                                                                        |

### More Concepts and Deep Learning
| הערכת זמן בימים | טכני                | מחקרי               | אלגוריתמי          | תרגיל                                                               |
|:---------------:|---------------------|---------------------|--------------------|---------------------------------------------------------------------|
|        1        |                     | :heavy_check_mark:  |                    | [loss function effects](advanced/loss_function_effects)             |
|        2        |                     | :heavy_check_mark:  |                    | [train test split](advanced/train_test_split)                       |
|        4        | :heavy_check_mark:  | :heavy_check_mark:  | :heavy_check_mark: | [attention](advanced/attention)                                     |
|                 |                     |                     |                    | [embedding layers]                                                  |
|        2        |                     |                     |                    | [generating text](advanced/generative_models/generating_text)       |
|                 |                     |                     |                    | [GAN]                                                               |
|                 | :heavy_check_mark:  |                     |                    | [enhanced LSTM]                                                     |

### Experimental work
| הערכת זמן בימים | טכני                | מחקרי               | אלגוריתמי          | תרגיל                                                                                     |
|:---------------:|---------------------|---------------------|--------------------|-------------------------------------------------------------------------------------------|
|        3        |                     | :heavy_check_mark:  |                    | [adversarial examples are not bugs, they are features](experimental/adversarial_features) |
|        3        | :heavy_check_mark:  | :heavy_check_mark:  | :heavy_check_mark: | [object detection using existing gits](experimental/git_utilization)                      |
|       2.5       | :heavy_check_mark:  |                     |                    | [apply model as a service](experimental/apply_model)                                      |
|        3        | :heavy_check_mark:  |                     |                    | [DGX & problem solving](experimental/remote_servers)                                      |

### Electives
| הערכת זמן בימים | טכני                | מחקרי               | אלגוריתמי          | תרגיל                                             |
|:---------------:|---------------------|---------------------|--------------------|---------------------------------------------------|
|        1        |                     |                     | :heavy_check_mark: | [anomaly detection](optional/anomaly_detection)   |
|        1        |                     |                     | :heavy_check_mark: | [feature selection]                               |
|        2        |                     |                     | :heavy_check_mark: | [adversarial attacks]                             |
|        1        |                     |                     | :heavy_check_mark: | [manifold learning](optional/manifold_learning)   |
|        1        |                     |                     | :heavy_check_mark: | [explainability](optional/explainability)         |
|        2        |                     | :heavy_check_mark:  | :heavy_check_mark: | [expressive power](optional/expressive_power)     |
|        ?        |                     |                     | :heavy_check_mark: | [deep normalization](optional/deep_normalization) |
|        1        | :heavy_check_mark:  |                     |                    | [git](optional/git)                               |

### Deprecated Exercises
| הערכת זמן בימים | טכני               | מחקרי               | אלגוריתמי          | תרגיל                                     |
|:---------------:|--------------------|---------------------|--------------------|-------------------------------------------|
|        3        |                    | :heavy_check_mark:  |                    | [critic review](deprecated/critic_review) |
|        1        | :heavy_check_mark: |                     |                    | [group by](deprecated/group_by)           |
|        1        | :heavy_check_mark: |                     |                    | [feature extraction]                      |
|        1        |                    | :heavy_check_mark:  |                    | [fixing a corrupted model]                |
|        2        | :heavy_check_mark: |                     |                    | [mileage]                                 |
s
