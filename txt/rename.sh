for i in *.png.txt; do 
  mv -- "$i" "${i%.png.txt}.txt"
done
