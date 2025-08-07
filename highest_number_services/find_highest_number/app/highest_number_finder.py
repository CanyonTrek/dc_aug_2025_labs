class HighestNumberFinder:
    def find_highest_number(self, numbers):
        """ Return the highest number from the list """
        if not numbers:
            raise ValueError("Empty List")
        highest_so_far = numbers[0]

        # Iterate through all the items using an ITERATOR loop.
        for number in numbers:
            if number > highest_so_far:
                highest_so_far = number
        return highest_so_far
