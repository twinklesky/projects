echo "Hello world."
timeStart=$(date +%s)
ls -l
ps -ef

if [ $? -eq 0 ];then
    echo "Commands executed successfully."
else
    echo "Commands executed failture."
fi

sleep 1

for row in {1..9}
do
    for col in {1..9}
    do
        if [ $col -le $row ];then
            echo -ne "$col*$row=$((col*row))\t"
        fi
    done
    echo ""
done

read -n1 -p "Are you continue[Y/N]?" answer
case $answer in
Y | y)
	echo -e "\nWelcome to my script.";;
N | n)
	echo -e "\nOk,we will turn out.";;
*)
	echo -e "\nSorry,input is error."
esac

echo "How to use find."
find . \( -name "*.txt" -o -name "*test.sh" \)
find . -iregex ".*\(\.py\|\.sh\)$"
find . ! -name "*.sh"
find . -type f -atime -7
find . -type f -size -2k
find . -name "*.sh" -exec cat -n {} \;
ls | find -name "*.sh"
find . -type f -name "*.sh" -exec printf "Sh file: %s\n" {} \;


echo "$(id)"

echo "print item for data"
data="name,sex,age,address"
oldIFS=$IFS
IFS=,
for item in $data
do
	echo "$item"
done
IFS=oldIFS



timeEnd=$(date +%s)
timeDiff=$((timeEnd-timeStart))
echo -e "\nTime used for executing is ${timeDiff}s"

