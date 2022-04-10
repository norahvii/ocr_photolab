for i in *.png; do 
  tesseract "$i" "$i"; 
done
