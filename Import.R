con <- DBI::dbConnect(
  +     odbc::odbc(),
  +     Driver   = "ODBC Driver 18 for SQL Server",   
  +     Server   = "HALE\\SQLEXPRESS",                
  +     Database = "AI20A02_New",                     
  +     UID      = "sa",                              
  +     PWD      = "River@2140",          
  +     TrustServerCertificate = "yes"                
  + )
> library(DBI)
> library(odbc)