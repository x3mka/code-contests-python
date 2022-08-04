#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vi = vector<int>;

int main()
{
    ios::sync_with_stdio(0);cin.tie(0);
    int n, x;
    cin >> n >> x;

    vi a(n);
    for (int i=0; i<n; i++)
        cin >> a[i];

    vi dp(x + 1);
    dp[0] = 1;

    for (int c : a)
        for (int i=1; i<x+1; i++)
            if (c <= i)
                dp[i] = (dp[i] + dp[i-c]) % 1000000007;

    cout << dp[x] << "\n";

    return 0;
}

