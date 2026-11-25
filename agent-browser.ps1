param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$Args
)
$entry = "D:\Project\ชวกม.2\%USERPROFILE%\.npm-global\node_modules\agent-browser\bin\agent-browser.js"
node $entry @Args
