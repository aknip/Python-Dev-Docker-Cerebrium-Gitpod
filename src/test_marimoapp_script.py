
__generated_with = "0.10.19"

# %%
import marimo as mo

# %%
mo.md(
    r"""
    # Marimo

    - Build and edit an app in Marimo
    - Re-use the app in a webservice, worker or app: Use `service.py` (in the same directory)
    - Test this via the terminal inside of Marimo (left bottom): `python src/service.py`
    """
)

# %%
print('App running...')

# %%
def calculate(var1):
    #print('calculating...')
    return(var1*10)

# %%
result = calculate(4711)
print('Result: ' + str(result))

# %%
mo.md(r"""#Tests""")

# %%
def inc(x):
    return x + 1

# %%
def test_sanity():
    assert inc(3) == 4, "This test passes"

# %%
def test_inc():
    assert inc(3) == 3, "This test fails"

# %%
def test_calculate():
    assert calculate(26)==260, "This test passes"