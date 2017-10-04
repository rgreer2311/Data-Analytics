#DS Templates

? #Help

#Packages
install.packages("")

#Vectors, indexed at 1 not 0
c()   #Combine
seq() #Sequence, creates a sequence between first number and second, third is by step
rep() #Replicate, repeates first number by the second
vName <- [c(value1, value2, ....)] ex. vName[1:3]
rbind() #Combines vectors to create a matrix by row
cbind() #Combines vectors to create a matrix by column
#Add column names to Matrix
names(v) <- c('colName', ...) <- NULL #To clear

#Matricies
colnames(v) <- c('colName', ...)
rownames(v) <- c('rowName', ...)
m[R,C]

#Subsetting
m[R:R, C:C]

#Functions
name <- function(params, param=dafault value){
	code
}

#Data Frames
setwd()     #Set the working directory
df <-read.<format>(file.choose())
nrow()      #Get number or rows
ncol()      #Get number of columns
head()      #Get first # of records
tail()      #Get last # of records
levels()    #Shows all factors (catagories) for a column
str()       #Structure of the table
runif()     #Random uniform distrobution
summary()   #Summary statistics for the dataset
$ 			#Extract a column

#Subsetting

#Derived columns
df$newcol <- R:C

#Filtering
filter1 <- df$column ><= value
df[filter1]

#Merging DataFrames
merge(df1, df2, by.x"col", by.y"col")

