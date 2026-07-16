$postDir = "f:\project\go\hugo_extended_withdeploy_0.163.2_windows-amd64\dev4\content\post"

$stablePhotos = @{
    "bg1.webp" = "https://images.unsplash.com/photo-1518770660439-4636190af475?w=1920&q=80"
    "bg2.webp" = "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=1920&q=80"
    "bg3.webp" = "https://images.unsplash.com/photo-1498050108023-c5249f4df085?w=1920&q=80"
    "bg4.webp" = "https://images.unsplash.com/photo-1485846234645-a62644f84728?w=1920&q=80"
    "bg5.webp" = "https://images.unsplash.com/photo-1542831371-29b0f74f9713?w=1920&q=80"
    "bg6.webp" = "https://images.unsplash.com/photo-1550684848-fac1c5b4e853?w=1920&q=80"
    "bg7.webp" = "https://images.unsplash.com/photo-1504384308090-c894fdcc538d?w=1920&q=80"
    "bg8.webp" = "https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=1920&q=80"
    "bg9.webp" = "https://images.unsplash.com/photo-1516414746402-935ce3621729?w=1920&q=80"
    "bg10.webp" = "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=1920&q=80"
    "bg11.webp" = "https://images.unsplash.com/photo-1506744038136-46273834b3fb?w=1920&q=80"
    "bg12.webp" = "https://images.unsplash.com/photo-1477959858617-67f85cf4f1df?w=1920&q=80"
    "bg13.webp" = "https://images.unsplash.com/photo-1542281286-9e0a16bb7366?w=1920&q=80"
    "bg14.webp" = "https://images.unsplash.com/photo-1544005313-94ddf0286df2?w=1920&q=80"
    "bg15.webp" = "https://images.unsplash.com/photo-1433086966358-54859d0ed716?w=1920&q=80"
    "bg16.webp" = "https://images.unsplash.com/photo-1534796636912-3b95b3ab5986?w=1920&q=80"
    "bg17.webp" = "https://images.unsplash.com/photo-1543005472-1b1d37fa4eae?w=1920&q=80"
    "bg18.webp" = "https://images.unsplash.com/photo-1526379095098-d400fd0bf935?w=1920&q=80"
    "bg19.webp" = "https://images.unsplash.com/photo-1501785888041-af3ef285b470?w=1920&q=80"
    "bg20.webp" = "https://images.unsplash.com/photo-1454496522488-7a8e488e8606?w=1920&q=80"
}

$files = Get-ChildItem -Path $postDir -Recurse -Filter "*.zh-CN.md" | 
         Where-Object { $_.FullName -notmatch "\\llm\\" }

foreach ($file in $files) {
    $content = [System.IO.File]::ReadAllText($file.FullName, [System.Text.Encoding]::UTF8)
    $modified = $false
    
    foreach ($oldUrl in $stablePhotos.Keys) {
        $pattern = "https://d-sketon\.top/img/backwebp/$oldUrl"
        if ($content -match $pattern) {
            $content = $content -replace [regex]::Escape($pattern), $stablePhotos[$oldUrl]
            $modified = $true
        }
    }
    
    if ($modified) {
        [System.IO.File]::WriteAllText($file.FullName, $content, [System.Text.Encoding]::UTF8)
        Write-Host "Updated: $($file.Name)"
    }
}

Write-Host "Done!"