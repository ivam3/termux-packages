#!/data/data/com.termux/files/usr/bin/bash

# Verifica si no se han proporcionado argumentos
[[ $# -eq 0 ]] && { echo -en >&2 "\e[31mmissing argument, type $(basename $0) -h for help\e[0m\n"; exit 1;}

# Función para mostrar la ayuda
usage(){
    echo -en """
usage $(basename $0) <options>

OPTIONS\t|DESCRIPTIONS
-n\tpackage name
-v\tpackage version
-a\tarchitecture
-p\tsupport page
-h\tshow this menu
"""
    exit 0
}

# Procesa las opciones de la línea de comandos
while getopts "n:v:a:p:h" opts; do
    case $opts in 
        n) pkgName=$OPTARG 
            if [[ -d $pkgName ]]
            then
                echo -en "\e[31mPackage $pkgName already exists\e[0m\n"
                exit 1
            fi
            ;;
        v) pkgv=$OPTARG ;;
        a) arch=$OPTARG ;;
        p) page=$OPTARG ;;
        h) usage ;;
        *) usage ;; # En caso de opción inválida, muestra la ayuda
    esac
done

# Si pkgName no está definido, muestra un mensaje de error
if [[ -z "$pkgName" ]]; then
    echo -en "\e[31mError: Package name (-n) is required\e[0m\n"
    exit 1
fi

echo $pkgName
read -p "Press Enter to continue..."

# Crea el directorio del paquete
mkdir -p "$pkgName/img"

# Resto del código que genera los archivos necesarios...

