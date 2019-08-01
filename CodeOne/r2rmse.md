RMSE is measure of the average deviation of the estimates from the observed values or is the square root of the variance of the residuals.. But R^2 is the fraction of the total sum of squares that is explained by the regression.

RMSE = sqrt((1/n)*(∑(y-^y)^2))

R^2 = 1-(SSE/TSS)

SSE: Sum of squared errors, sum of the squares of the differences between the observed values and the expected values = ∑(y-^y)^2

TSS: Total sum of squares, the sum of the squares of the differences between the observed values and the average of the observed values .

then;

R^2 = 1 - ((n*RMSE^2)/TSS)

The R-square is usually between 0 and 1. However, RMSE does not have a certain interval. It is easier to interpret the R^2. Simply, the model can be expressed as the regression ratio. RMSE shows how much our estimates deviate from the actual values in the data set on average. In some cases we need to look at the R^2, and in some cases we only need to look at the RMSE. If we look at RMSE only, we can not see anything about how much we vary, because it does not add up to how much variability we have in the end. For this reason, it is often useful to review and comment on both.