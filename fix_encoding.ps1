$postDir = "f:\project\go\hugo_extended_withdeploy_0.163.2_windows-amd64\dev4\content\post"

$files = Get-ChildItem -Path $postDir -Recurse -Filter "*.zh-CN.md" | 
         Where-Object { $_.FullName -notmatch "\\llm\\" }

$fixedCount = 0

foreach ($file in $files) {
    $content = [System.IO.File]::ReadAllBytes($file.FullName)
    
    $hasGarbage = $false
    for ($i = 0; $i -lt $content.Length; $i++) {
        if ($content[$i] -eq 0x3F -and $i + 2 -lt $content.Length -and 
            $content[$i+1] -eq 0x3F -and $content[$i+2] -eq 0x3F) {
            $hasGarbage = $true
            break
        }
    }
    
    if ($hasGarbage) {
        try {
            $gbkContent = [System.Text.Encoding]::GetEncoding("GBK").GetString($content)
            [System.IO.File]::WriteAllText($file.FullName, $gbkContent, [System.Text.Encoding]::UTF8)
            Write-Host "Fixed (GBK->UTF8): $($file.Name)"
            $fixedCount++
        } catch {
            Write-Host "Failed to fix: $($file.Name)"
        }
    } else {
        $utf8Content = [System.Text.Encoding]::UTF8.GetString($content)
        if ($utf8Content -match '�') {
            $contentStr = $utf8Content -replace '线段�', '线段树'
            $contentStr = $contentStr -replace '技术分�', '技术分享'
            $contentStr = $contentStr -replace '适配器模式详�', '适配器模式详解'
            $contentStr = $contentStr -replace '责任链模式详�', '责任链模式详解'
            $contentStr = $contentStr -replace '观察者模式详�', '观察者模式详解'
            $contentStr = $contentStr -replace '装饰器模式详�', '装饰器模式详解'
            $contentStr = $contentStr -replace '策略模式详�', '策略模式详解'
            $contentStr = $contentStr -replace '模板方法模式详�', '模板方法模式详解'
            $contentStr = $contentStr -replace '单例模式详�', '单例模式详解'
            $contentStr = $contentStr -replace '代理模式详�', '代理模式详解'
            $contentStr = $contentStr -replace '工厂方法与抽象工厂模�', '工厂方法与抽象工厂模式'
            $contentStr = $contentStr -replace '建造者模式详�', '建造者模式详解'
            $contentStr = $contentStr -replace '结构型模�', '结构型模式'
            $contentStr = $contentStr -replace '行为型模�', '行为型模式'
            $contentStr = $contentStr -replace '创建型模�', '创建型模式'
            $contentStr = $contentStr -replace '哈希表HashM�', '哈希表HashMap'
            $contentStr = $contentStr -replace 'TCP三次握手与四次挥�', 'TCP三次握手与四次挥手'
            $contentStr = $contentStr -replace 'TCP流量控制与拥塞控�', 'TCP流量控制与拥塞控制'
            $contentStr = $contentStr -replace 'WebSocket与实时通�', 'WebSocket与实时通信'
            $contentStr = $contentStr -replace 'HTTP协议详解与HTTPS原�', 'HTTP协议详解与HTTPS原理'
            $contentStr = $contentStr -replace '网络分层模型与数据封�', '网络分层模型与数据封装'
            $contentStr = $contentStr -replace '从输入URL到页面渲染全过�', '从输入URL到页面渲染全过程'
            $contentStr = $contentStr -replace '排序算法详�', '排序算法详解'
            $contentStr = $contentStr -replace '动态规划经典问�', '动态规划经典问题'
            $contentStr = $contentStr -replace '图算法与最短路径详�', '图算法与最短路径详解'
            $contentStr = $contentStr -replace '二叉树与遍历实�', '二叉树与遍历实战'
            $contentStr = $contentStr -replace '位图BitMap详�', '位图BitMap详解'
            
            if ($contentStr -ne $utf8Content) {
                [System.IO.File]::WriteAllText($file.FullName, $contentStr, [System.Text.Encoding]::UTF8)
                Write-Host "Fixed (char substitution): $($file.Name)"
                $fixedCount++
            }
        }
    }
}

Write-Host "Done! Total fixed: $fixedCount"
