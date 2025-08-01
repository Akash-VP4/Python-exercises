def love_meet(bob, alice):

    return set([distrct for distrct in bob if distrct in alice])
    ...


def affair_meet(bob, alice, silvester):

    return set(
        [distrct for distrct in alice if distrct in silvester and distrct not in bob]
    )
    ...
