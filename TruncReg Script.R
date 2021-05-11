library(truncreg)

# Fetch command line arguments
myArgs <- commandArgs(trailingOnly=TRUE)
C <- as.numeric(myArgs[1]) # convert truncation parameter to numeric
dir <- myArgs[2]  # truncation direction

# read in truncated data from the csv file
file <- 'data.csv'
d <- read.csv(file, header=TRUE, col.names = c("NONE", "X0", "X1", "Y"))
X <- as.matrix(as.numeric(cbind(d$X0, d$X1)))
y <- as.matrix(d$Y)
df <- data.frame(X=X, y=y)

# truncated regression procedure
trunc_reg <- truncreg(df$y ~ X, data=df, point=C, direction=dir, scaled=TRUE)

# return model coefficients
coef_df <- coef(trunc_reg)
print(coef_df)
