def make_sandwich(size, *fillings):
    """Summarize the sandwich we are about to make."""
    print("\nMaking a " + size +
            "-size sandwich with the following fillings:")

    for filling in fillings:
        print("- " + filling)

make_sandwich('large', 'Beef')
make_sandwich('small', 'Pork', 'Onion', 'Potato')
