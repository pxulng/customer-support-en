# Client scoping (fictional client)

> Scoping document. All data is synthetic. Figures marked (A) are assumptions, not measurements.

## 1. The client
- **Name:** Vélora Sport, online and in-store sports retailer (fictional)
- **Request volume:** 3,000 per month (A)
- **Channels:** email and web form
- **Support team:** 6 advisors (A)
- **Problem:** advisors spend their time on repetitive requests (order tracking, returns), which delays complex cases.

## 2. Request types
| Type | Example | Estimated share (A) |
|---|---|---|
| Order tracking | "Where is my parcel?" | 35% |
| Return and refund | "I want to send my shoes back" | 25% |
| Defective product / warranty | "The shoes are damaged after two weeks" | 15% |
| Complaint / dispute | "I never received my refund" | 25% |

## 3. Always escalated to a human
- Dispute, legal threat or very angry customer
- Refund outside the written conditions
- Information absent from the procedures
- Sensitive personal data
- Any request where the assistant has a doubt

## 4. Current process
1. **Receipt**: the request arrives by email or form.
2. **Triage**: an advisor reads and classifies the request.
3. **Reply**: the advisor looks up the procedure and writes the reply.
4. **Escalation**: sensitive cases go up to a manager.

## 5. User stories
1. As an advisor, I want each request classified automatically so I don't sort it by hand.
2. As an advisor, I want a draft reply that cites the procedure used, so I can check it quickly.
3. As an advisor, I want to be alerted when the assistant is unsure, so I handle those cases myself.
4. As a manager, I want sensitive cases never to receive an automatic reply.
5. As a manager, I want to know the cost per request to judge whether the tool pays off.
6. As a customer, I want a correct and polite answer, or a message telling me an advisor will reply.

## 6. Success criteria (targets I set, to be confirmed by measurement)
- No request that should be escalated receives an automatic reply.
- Correct classification rate: target ≥ 85% (A)
- Draft quality: target ≥ 3 out of 4 on average (grid to be defined)
- Cost per request: to be measured

## 7. Scope
- **Included:** classification, sourced draft, escalation rule, quality and cost measurement.
- **Excluded:** automatic sending of replies, integration with a real ticketing tool, real data.
