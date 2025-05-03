# 👨‍🍳 ChefScript

## Instalace a spuštění

```bash
git clone https://github.com/MarcelHor/chefscript.git
cd chefscript
```

Nejjednodušší způsob, jak projekt spustit, je pomocí Makefile. 

```c
make install                # Vytvoří virtuální prostředí (.venv) a nainstaluje závislosti z requirements.txt
make generate               # Vygeneruje lexer a parser ze souboru grammar/ChefScript.g4
make                        # Spustí výchozí soubor input/calculator.chef
make FILE=input/jiny.chef   # Spustí jiný soubor zadaný proměnnou FILE
```

Může být potřeba upravit proměnné v horní části Makefile – ANTLR, Python a další.

**Ingredience (Proměnné)**

```c
# Číselné hodnoty
-?[0-9]+

ingredient flour = 500;
ingredient eggs = 3;
ingredient sugar = 200;
ingredient flavor = "vanilla";
ingredient tasty = false
``` 

## Porovnávání hodnot
```c
flour > sugar
flour >= sugar
flour < sugar
flour <= sugar

# Relace == je "same"
flour same sugar
# Relace != je "notSame"
flour notSame sugar
```

## Aritmetické operace
```c
+
-
*
/

flour + sugar;
flour - sugar;
flour * 2;
 
```


## Logické výrazy a podmínky
```c
# AND = "mix"
# OR = "either"
# NOT = "ew"

recipeReady = flour > 100 mix sugar > 50;
sweetEnough = flour < 200 either sugar > 100;
burned = ew sweetEnough;

taste (recipeReady) {
    dish ("Perfect dish!");
} else {
    dish ("Try again!");
}
```

## Smyčky (For loop)
```c
taste (flour > sugar) {
    stir (ingredient i = 0; i < 3; i = i + 1) {
        dish ("Mixing... step " + i);
    }
}
```

## Funkce (Recepty)
```c
recipe bakeCake() {
    dish ("Baking the cake!");
    serve 1;
}

ingredient cake = bakeCake();
dish (cake + " is ready to eat!");
```