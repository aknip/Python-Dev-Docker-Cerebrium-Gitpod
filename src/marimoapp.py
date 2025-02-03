import marimo

__generated_with = "0.10.19"
app = marimo.App()


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md(
        r"""
        # Marimo

        - Build and edit an app in Marimo
        - Re-use the app in a webservice, worker or app: Use `service.py` (in the same directory)
        - Test this via the terminal inside of Marimo (left bottom): `python src/service.py`
        """
    )
    return


@app.cell
def _():
    print('App running...')
    return


@app.cell
def _():
    def calculate(var1):
        #print('calculating...')
        return(var1*10)
    return (calculate,)


@app.cell
def _(calculate):
    result = calculate(4711)
    print('Result: ' + str(result))
    return (result,)


@app.cell
def _(mo):
    mo.md(r"""#Tests""")
    return


@app.cell
def _():
    def inc(x):
        return x + 1
    return (inc,)


@app.cell
def _(inc):
    def test_sanity():
        assert inc(3) == 4, "This test passes"
    return (test_sanity,)


@app.cell
def _(inc):
    def test_inc():
        assert inc(3) == 3, "This test fails"
    return (test_inc,)


@app.cell
def _(calculate):
    def test_calculate():
        assert calculate(26)==260, "This test passes"
    return (test_calculate,)


if __name__ == "__main__":
    app.run()
