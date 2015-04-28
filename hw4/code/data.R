library("ggplot2")
df = movies

write.table(df, file='../data/movies.csv', sep=',', row.names=FALSE)
