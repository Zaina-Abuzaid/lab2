# Model selection

Fill this in after you have trained your candidates in MLflow. Short sentences are fine. Use numbers from your runs.

## The question
What does this model decide, and who is hurt by a wrong answer? (One or two sentences.)
The model predicts wether a customer is likely to churn. A wrong prediction could cause the company to lose a customer or spend
resources unnecessarily.
## Candidates
|Candidate       | Why I tried it| AUC   | F1   |F1 per slice(lowest)|p95 latency (ms)|Size (KB)|MLflow run ID                    |
|----------------|---------------|-------|------|--------------------|----------------|---------|---------------------------------|
|logreg          |simple/fast /  |0.7833 |0.5124|      0             |     5.5794     | 3.5479  |cf7059f6cf5b43569278eccc83560f84 |                                         
|                |baseline model |       |      |                    |                |         |                                 |     
|random_forest   |To learn coplex|0.7593 |0.5289|      0.1667        |     21.0379    |3105.7207|2d8eff01858948e89ab7ff3770bf1de8 |
|                |patterns       |       |      |                    |                |         |                                 |
|gradient_boosting| To reduce    |0.7753 |0.4960|      0.2222        |     4.6883     |140.6602 |a1146c22019e407997dcd85b790666a5 |
|                |   errors      |       |      |                    |                |         |


## The champion
Which one did I pick, and what decided it? (Name the numbers that mattered and the ones I accepted losing.)
I chose Random Forest as the champion because it had the highest F1 score (0.5289) and met the 30 ms latency budget (21.0379 ms).
However it had a lower AUC (0.7593), a larger size (3105.7207 KB), and a lowest slice F1 of 0.1667.


## My promotion rules
- Latency budget (p95): _30__ ms, because _predictions should be fast.__
- Minimum gain to replace the champion (F1 points): _0.02__, because _a very small emprovement is not worth changing the model.__

## What I would check next
One thing that could make this choice wrong in production (for example a slice with few customers, or data that changes).
I would check the model’s performance for customers with two-year contracts because their F1 score was only 0.1667.