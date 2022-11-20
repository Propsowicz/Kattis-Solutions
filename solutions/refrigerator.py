
data = input().strip().split(' ')

cost_a = int(data[0])
capa_a = int(data[1])
cost_b = int(data[2])
capa_b = int(data[3])
total = int(data[4])

eff_a = capa_a/cost_a
eff_b = capa_b/cost_b

ref_to_transport = total
transport_a = 0
transport_b = 0
cost = 0

def cost_check(ref_to_transport, cost_1, cost_2, capa_1, capa_2, transport_1, transport_2, cost):
    while ref_to_transport > 0:
        transport_1 += 1
        cost += cost_1
        ref_to_transport -= capa_1
        if ref_to_transport % capa_2 == 0 and (ref_to_transport // capa_2 * cost_2 < (ref_to_transport // capa_1 + 1)* cost_1):
            transport_2, transport_1, ref_to_transport, cost = cost_check(ref_to_transport, cost_2, cost_1, capa_2, capa_1, transport_2, transport_1, cost)
    return transport_1, transport_2, ref_to_transport, cost

if eff_a > eff_b:    
    while ref_to_transport > 0:
        transport_a, transport_b, ref_to_transport, cost = cost_check(ref_to_transport, cost_a, cost_b, capa_a, capa_b, transport_a, transport_b, cost)
else:
    while ref_to_transport > 0:
        transport_b, transport_a, ref_to_transport, cost = cost_check(ref_to_transport, cost_b, cost_a, capa_b, capa_a, transport_b, transport_a, cost)

print(f'{transport_a} {transport_b} {cost}')
