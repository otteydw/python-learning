# >>> print(solution(9565, [73153709, 73410599, 73564913, 73770857, 73925603, 74028791, 74235407, 74390621, 74442383, 74563189, 74718727, 74908961, 75099547, 75220913, 75325037, 75429209, 75533477, 75620407, 75742193, 75864091, 75968647, 76125589, 76282747, 76370117, 76457527])
# ABCDEFGHIJKLMNOPQRSTUVWXYZ

def solution(n, encrypted_message):

    def get_adjacent_prime_products(encrypted_message):
        all = encrypted_message
        all.sort()
        all = list(dict.fromkeys(all))
        return all

    def get_previous_prime(current_prime, previous_prime_product):
        previous_prime = previous_prime_product / current_prime
        return previous_prime

    def is_prime(n):
        factors=0

        for x in range(1, n):
            if n % x == 0:
                factors+=1
                if factors > 1:
                    return False
        return True

    def find_z(n):
        for z in range(n, 1, -1):
            print(z)
            if is_prime(z):
                return z

    z = find_z(n)

    ordered_prime_products = get_adjacent_prime_products(encrypted_message)
    # print(len(ordered_prime_products))
    ordered_primes = [z]
    current_prime = z
    while len(ordered_prime_products) > 0:
        print('Current prime: ' + str(current_prime))
        current_product = ordered_prime_products[-1]
        previous_prime = get_previous_prime(current_prime, current_product)
        ordered_primes.append(previous_prime)
        current_prime = previous_prime
        ordered_prime_products.remove(current_product)
        print()

    return ordered_primes



# def is_prime(n):
#     factors=0

#     for x in range(1, n):
#         if n % x == 0:
#             factors+=1
#             if factors > 2:
#                 break
#     print(n)
# is_prime(2)
# is_prime(3)
# is_prime(4)
# is_prime(5)


# print(solution(10, [1, 2, 3, 5, 4, 5, 3, 1]))
print(solution(9565, [73153709, 73410599, 73564913, 73770857, 73925603, 74028791, 74235407, 74390621, 74442383, 74563189, 74718727, 74908961, 75099547, 75220913, 75325037, 75429209, 75533477, 75620407, 75742193, 75864091, 75968647, 76125589, 76282747, 76370117, 76457527]))