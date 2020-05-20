raw <− read.table ( ’Desktop/anaconda_files/aadt.txt’ , header=FALSE)
df <− data.frame(y=raw$V1, x1=raw$V2, x2=raw$V3, x3=raw$V4, x4=raw$V5)
mlr2 <− lm(y ∼ x1+x2+x3+x4, data=df ) plot(residuals(mlr2),ylab=’Residuals ’, xlab=’Time’) 
plot(residuals(mlr2),fitted(mlr2),ylab=’Residuals ’,xlab=’Fitted values ’)

mlr3 <- lm(sqrt(y) ~ x1+x2+x3+x4, data=df)
plot(residuals(mlr3),fitted(mlr3),ylab='Residuals', xlab='Fitted values')

library(MASS)
b <- boxcox(y ~ x1+x2+x3+x4, data = df)
lambda <- b$x
lik <- b$y
bc <- cbind(lambda, lik)
sorted_bc <- bc[order(-lik),]
head(sorted_bc, n = 10)

mlr4 <- lm((y^0.2626263 - 1)/0.2626263 ~ x1+x2+x3+x4, 
            data=df)
plot(residuals(mlr4),fitted(mlr4),ylab='Residuals'
     ,xlab='Fitted values')

mlr1 <- lm(sqrt(y) ~ x1+x2+x4, data=df)
mlr <- lm(sqrt(y) ~ x1+x2+x3+x4, data=df)
anova(mlr1,mlr)

plot(residuals(mlr1),fitted(mlr1),ylab='Residuals'
     ,xlab='Fitted values')

con <- data.frame(x1=50000,x2=3,x4=2)
predict(mlr1,con,interval='confidence',level=0.95)
predict(mlr1,con,interval='prediction',level=0.95)

