def calculate_posterior_probability(prior_prob, likelihood_jump, likelihood_not_jump):
    # P(A|B) = (P(B|A) * P(A)) / P(B)
    nume = likelihood_jump * prior_prob
    prior_not_prob = 1 - prior_prob
    prob_all = nume + (likelihood_not_jump * prior_not_prob)   
    # 아이가 공을 들고 있을 전체 확률 = 도로에 뛰어든 아이 중 공을 들고 있을 확률 + 도로에 뛰어들지 않은 아이 중 공을 들고 있을 확률
    posterior_prob = nume / prob_all
    return posterior_prob

prior_prob = 0.1            # 아이가 도로에 뛰어들 사전 확률
likelihood_jump = 0.8       # 도로로 뛰어든 아이가 공을 들고 있을 확률
likelihood_not_jump = 0.3   # 도로로 뛰어들지 않은 아이가 공을 들고 있을 확률

result= calculate_posterior_probability(prior_prob, likelihood_jump, likelihood_not_jump)
print(f"아이가 공을 들고 있을 때, 도로로 뛰어들 사후 확률: {result:.2f}")