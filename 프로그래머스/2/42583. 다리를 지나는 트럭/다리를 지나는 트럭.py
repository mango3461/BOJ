def solution(bridge_length, weight, truck_weights):
    time = 0
    total_weight = 0
    bridge = []  # (트럭 무게, 남은 다리 길이)
    trucks = truck_weights.copy()

    while trucks or bridge:
        time += 1

        # 1. 다리 위 트럭 이동 (남은 거리 1 감소)
        bridge = [(w, t-1) for w, t in bridge]

        # 2. 끝난 트럭 제거
        if bridge and bridge[0][1] == 0:
            w, _ = bridge.pop(0)
            total_weight -= w

        # 3. 다음 트럭 올라갈 수 있으면 추가
        if trucks and total_weight + trucks[0] <= weight:
            w = trucks.pop(0)
            bridge.append((w, bridge_length))
            total_weight += w

    return time
