<!-- https://www.beecrowd.com.br/judge/en/problems/view/1199 -->
<!-- numero decimal debe ser igual o menor 2^3
1ínea que contiene un número decimal negativo 
termina la entrada 

NOTA esta version no se termino completamente, en python si
-->

<?php

echo "Digite un número decimal: ";
fscanf(STDIN, "%d", $decimal);
echo "Digite un hexadecimal: ";
fscanf(STDIN, "%s", $hexa);

if (($hexa != ''  || $hexa > 0) || (($decimal >= 0 && $decimal <= pow(2, 31)) && ($decimal !=''))) {
    if ($decimal != 0 && $decimal != '' ) {
        $hexa = "0x" . (dechex($decimal));
        echo "El numero hexadecimal del decimal: $decimal es $hexa";
    } else {
        $decimal = hexdec($hexa);
        echo "El numero decimal del hexadecimal: $hexa es $decimal";
    }
}
else {
    echo "El numero no es valido";
}

?>