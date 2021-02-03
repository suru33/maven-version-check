# Maven Version Comparator

Compare maven release versions

```shell
pip install mvn-compare
```

### Examples

```shell

~$ mvn-compare "1.0-alpha1" "1.0-beta1"
-1  

~$ mvn-compare "1.0" "1.0-beta1"
1

~$ mvn-compare "1.0-final" "1.0"
0

```
Test shell script
```shell
V1="9.3-alpha10"
V2="9.2"

OP=$(mvn-compare $V1 $V2)
echo "v1: $V1, v2: $V2"

if [ $OP -le 0 ] 
then
  echo "upgrade not possible"
else
  echo "Upgraded"
fi
```