type image;
image photo <"shane.jpg">;
image rotated <"rotated.jpg">;

app (image output) rotate(image input, int angle) {
   convert "-rotate" angle @input @output;
}

rotated = rotate(photo, 180);
