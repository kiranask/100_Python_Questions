class PrimeChecker:
    """
    A class to check if a given number is prime.
    """

    def __init__(self, item):
        """
        Initialize the PrimeChecker instance with the number to check.

        :param item: The number to check for primality.
        """
        self.item = item

    def is_prime(self):
        """
        Check if the stored number is a prime number.

        A prime number is greater than 1 and divisible only by 1 and itself.

        :return: True if the number is prime, False otherwise.
        """
        num = self.item

        # Check if the number is greater than 1
        if num > 1:
            # Iterate from 2 to num/2 (inclusive)
            for i in range(2, int((num / 2) + 1)):
                # If num is divisible by any number in this range, it's not prime
                if num % i == 0:
                    return False
            # If no divisors are found, the number is prime
            return True
        else:
            # Numbers <= 1 are not prime
            return False


if __name__ == "__main__":
    # Create a PrimeChecker instance for the number 10
    prime = PrimeChecker(10)
    # Check if the number is prime and print the result
    print(prime.is_prime())
