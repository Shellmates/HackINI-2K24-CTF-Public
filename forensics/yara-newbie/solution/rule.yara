rule ChinaChopper
{
    strings:
        $webshell = /@eval\(\$_POST\['\w+'\]\);/i

    condition:
        $webshell
}
