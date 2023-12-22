fswatch -o $(find . | grep -E "(.*jinja.*|.*css.*)") | xargs -n1 -I{} ./generator.sh
