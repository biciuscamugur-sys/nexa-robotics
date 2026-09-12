from nexa.security.invariants import SafetyState, check_safety


def test_safe_state():
    state = SafetyState(
        speed=1.0,
        battery=80.0,
        obstacle_distance=2.0,
    )

    assert check_safety(state) is True


def test_speed_too_high():
    state = SafetyState(
        speed=3.0,
        battery=80.0,
        obstacle_distance=2.0,
    )

    assert check_safety(state) is False


def test_obstacle_too_close():
    state = SafetyState(
        speed=1.0,
        battery=80.0,
        obstacle_distance=0.2,
    )

    assert check_safety(state) is False


def test_invalid_battery():
    state = SafetyState(
        speed=1.0,
        battery=120.0,
        obstacle_distance=2.0,
    )

    assert check_safety(state) is False
