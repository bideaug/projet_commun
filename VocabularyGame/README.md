# Vocabulary Game

This game has been made in order to help reviewing Vocabulary. It has a dependence to the protobuf project. Please make sure you have it install.

To run the graphical version run :

```bash
python main.py -g
```

one can also run

```bash
make graphical
```

## Usage of the converter

For now, only the `json` to `protobuf` version of the converter has been implemented, to run it enter the following command :

```
python main.py -c SRC DEST
```
where SRC and DEST are paths corresponding to the source file to converter and to the destination path
