$projectDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $projectDir
mvn -q -DskipTests javafx:run