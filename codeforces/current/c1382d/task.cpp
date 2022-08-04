#include <bits/stdc++.h>
using namespace std;


int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int t = 1;
    cin >> t;

    while (t--) {
        int n;
        cin >> n;

        int p[2 * n];
        for(int i=0;i<=2*n;i++){
            cin >> p[i]
        }



        if solve(n, p) {
            cout << 'YES';
        } else {
            cout << 'NO';
        }

        cout << "\n";
    }

    return 0;
}

