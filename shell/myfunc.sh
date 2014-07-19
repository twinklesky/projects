

fname()
{
	echo "\$1,\$2=$1,$2";
	echo "\$@=$@";
	echo "\$*=$*"
	return 0;
}
fname "age" "address" "sex";
echo "we usually used \$@ to list args."

