import typer
from typing import Optional
import os
import inquirer
###################################
from parts.home import home_page
###################################


def main(status: Optional[str] = typer.Argument("home")):
    if status == "home":
      home_page()
      mode = [
        inquirer.List(
          "mode",
          message="Choose report type:",
          choices=[
            typer.style("Dictionary attack",fg=typer.colors.GREEN),
            typer.style("Brute force attack",fg=typer.colors.GREEN),
          ]
        ),
      ]
      y = inquirer.prompt(mode)
      if "Dictionary attack" in y["mode"]:
        wl = typer.prompt(f"{typer.style('Type the name of the dictionary file in the Wordlist folder',fg=typer.colors.GREEN)}")
        user = typer.prompt(f"{typer.style('Enter the target\'s username',fg=typer.colors.GREEN)}")
        insta_dict(wordlist=wl,username=user)
      if "" in y["mode"]:
        username=typer.prompt(f"{typer.style('Enter the target\'s username',fg=typer.colors.GREEN)}")
        pwd_size=int(typer.prompt(f"{typer.style('Enter a passowrd size 8=<',fg=typer.colors.GREEN)}"))
        if pwd_size >=8:
          insta_brute(target=username,pwd_size=pwd_size)
        else:
          typer.secho("Error!",fg=typer.colors.RED)
          quit()

if __name__ == "__main__":
  typer.run(main)
