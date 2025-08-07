from inspect import signature as _mutmut_signature
from typing import Annotated
from typing import Callable
from typing import ClassVar


MutantDict = Annotated[dict[str, Callable], "Mutant"]


def _mutmut_trampoline(orig, mutants, call_args, call_kwargs, self_arg = None):
    """Forward call to original or mutated function, depending on the environment"""
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = orig(*call_args, **call_kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = orig(*call_args, **call_kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    if self_arg:
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs)
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs)
    return result
from inspect import signature as _mutmut_signature
from typing import Annotated
from typing import Callable
from typing import ClassVar


MutantDict = Annotated[dict[str, Callable], "Mutant"]


def _mutmut_yield_from_trampoline(orig, mutants, call_args, call_kwargs, self_arg = None):
    """Forward call to original or mutated function, depending on the environment"""
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = yield from orig(*call_args, **call_kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = yield from orig(*call_args, **call_kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    if self_arg:
        # call to a class method where self is not bound
        result = yield from mutants[mutant_name](self_arg, *call_args, **call_kwargs)
    else:
        result = yield from mutants[mutant_name](*call_args, **call_kwargs)
    return result
class HighestNumberFinder:
    def xǁHighestNumberFinderǁfind_highest_number__mutmut_orig(self, numbers):
        """ Return the highest number from the list """
        if not numbers:
            raise ValueError("Empty List")
        highest_so_far = numbers[0]

        # Iterate through all the items using an ITERATOR loop.
        for number in numbers:
            if number > highest_so_far:
                highest_so_far = number
        return highest_so_far
    def xǁHighestNumberFinderǁfind_highest_number__mutmut_1(self, numbers):
        """ Return the highest number from the list """
        if numbers:
            raise ValueError("Empty List")
        highest_so_far = numbers[0]

        # Iterate through all the items using an ITERATOR loop.
        for number in numbers:
            if number > highest_so_far:
                highest_so_far = number
        return highest_so_far
    def xǁHighestNumberFinderǁfind_highest_number__mutmut_2(self, numbers):
        """ Return the highest number from the list """
        if not numbers:
            raise ValueError(None)
        highest_so_far = numbers[0]

        # Iterate through all the items using an ITERATOR loop.
        for number in numbers:
            if number > highest_so_far:
                highest_so_far = number
        return highest_so_far
    def xǁHighestNumberFinderǁfind_highest_number__mutmut_3(self, numbers):
        """ Return the highest number from the list """
        if not numbers:
            raise ValueError("XXEmpty ListXX")
        highest_so_far = numbers[0]

        # Iterate through all the items using an ITERATOR loop.
        for number in numbers:
            if number > highest_so_far:
                highest_so_far = number
        return highest_so_far
    def xǁHighestNumberFinderǁfind_highest_number__mutmut_4(self, numbers):
        """ Return the highest number from the list """
        if not numbers:
            raise ValueError("empty list")
        highest_so_far = numbers[0]

        # Iterate through all the items using an ITERATOR loop.
        for number in numbers:
            if number > highest_so_far:
                highest_so_far = number
        return highest_so_far
    def xǁHighestNumberFinderǁfind_highest_number__mutmut_5(self, numbers):
        """ Return the highest number from the list """
        if not numbers:
            raise ValueError("EMPTY LIST")
        highest_so_far = numbers[0]

        # Iterate through all the items using an ITERATOR loop.
        for number in numbers:
            if number > highest_so_far:
                highest_so_far = number
        return highest_so_far
    def xǁHighestNumberFinderǁfind_highest_number__mutmut_6(self, numbers):
        """ Return the highest number from the list """
        if not numbers:
            raise ValueError("Empty list")
        highest_so_far = numbers[0]

        # Iterate through all the items using an ITERATOR loop.
        for number in numbers:
            if number > highest_so_far:
                highest_so_far = number
        return highest_so_far
    def xǁHighestNumberFinderǁfind_highest_number__mutmut_7(self, numbers):
        """ Return the highest number from the list """
        if not numbers:
            raise ValueError("Empty List")
        highest_so_far = None

        # Iterate through all the items using an ITERATOR loop.
        for number in numbers:
            if number > highest_so_far:
                highest_so_far = number
        return highest_so_far
    def xǁHighestNumberFinderǁfind_highest_number__mutmut_8(self, numbers):
        """ Return the highest number from the list """
        if not numbers:
            raise ValueError("Empty List")
        highest_so_far = numbers[1]

        # Iterate through all the items using an ITERATOR loop.
        for number in numbers:
            if number > highest_so_far:
                highest_so_far = number
        return highest_so_far
    def xǁHighestNumberFinderǁfind_highest_number__mutmut_9(self, numbers):
        """ Return the highest number from the list """
        if not numbers:
            raise ValueError("Empty List")
        highest_so_far = numbers[0]

        # Iterate through all the items using an ITERATOR loop.
        for number in numbers:
            if number >= highest_so_far:
                highest_so_far = number
        return highest_so_far
    def xǁHighestNumberFinderǁfind_highest_number__mutmut_10(self, numbers):
        """ Return the highest number from the list """
        if not numbers:
            raise ValueError("Empty List")
        highest_so_far = numbers[0]

        # Iterate through all the items using an ITERATOR loop.
        for number in numbers:
            if number > highest_so_far:
                highest_so_far = None
        return highest_so_far
    
    xǁHighestNumberFinderǁfind_highest_number__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁHighestNumberFinderǁfind_highest_number__mutmut_1': xǁHighestNumberFinderǁfind_highest_number__mutmut_1, 
        'xǁHighestNumberFinderǁfind_highest_number__mutmut_2': xǁHighestNumberFinderǁfind_highest_number__mutmut_2, 
        'xǁHighestNumberFinderǁfind_highest_number__mutmut_3': xǁHighestNumberFinderǁfind_highest_number__mutmut_3, 
        'xǁHighestNumberFinderǁfind_highest_number__mutmut_4': xǁHighestNumberFinderǁfind_highest_number__mutmut_4, 
        'xǁHighestNumberFinderǁfind_highest_number__mutmut_5': xǁHighestNumberFinderǁfind_highest_number__mutmut_5, 
        'xǁHighestNumberFinderǁfind_highest_number__mutmut_6': xǁHighestNumberFinderǁfind_highest_number__mutmut_6, 
        'xǁHighestNumberFinderǁfind_highest_number__mutmut_7': xǁHighestNumberFinderǁfind_highest_number__mutmut_7, 
        'xǁHighestNumberFinderǁfind_highest_number__mutmut_8': xǁHighestNumberFinderǁfind_highest_number__mutmut_8, 
        'xǁHighestNumberFinderǁfind_highest_number__mutmut_9': xǁHighestNumberFinderǁfind_highest_number__mutmut_9, 
        'xǁHighestNumberFinderǁfind_highest_number__mutmut_10': xǁHighestNumberFinderǁfind_highest_number__mutmut_10
    }
    
    def find_highest_number(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁHighestNumberFinderǁfind_highest_number__mutmut_orig"), object.__getattribute__(self, "xǁHighestNumberFinderǁfind_highest_number__mutmut_mutants"), args, kwargs, self)
        return result 
    
    find_highest_number.__signature__ = _mutmut_signature(xǁHighestNumberFinderǁfind_highest_number__mutmut_orig)
    xǁHighestNumberFinderǁfind_highest_number__mutmut_orig.__name__ = 'xǁHighestNumberFinderǁfind_highest_number'
