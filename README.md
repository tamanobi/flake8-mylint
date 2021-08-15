flake8 のカスタムプラグインです。モジュールグローバルな変数に、listが使われていた場合警告を出します。

もし、モジュールグローバルなlistにappendやclear, pop, remove, delを呼び出した場合、実行中のプロセスにおいてlistが書き換わります。
その場合、予期せぬ副作用を引き起こすリスクがあります。

実際に、実務でそのようなトラブルが起きたことがあります。
上記のような性質とエンバグの可能性を考えると、モジュールグローバルな変数は変更不可能であるべきです。

実現するために、次のルールを敷きます。

* list の代わりに tuple を利用する
* dict の代わりに types モジュールの MappingProxyType を利用する

tuple は list に近いインタフェースを持っており、置き換えが容易です。加えてImmutableなデータ構造です。
一方、 dict に近いインタフェースを持っている Immutable なデータ構造は標準パッケージに存在しません。
最も近いのは、 dataclasses.dataclass の `fronzen=True` ですが、バリューへのアクセス方法が大きく異なり、既存コードをリファクタリングするコストが高くなります。

そこで Immutable なデータ構造を諦め、 読み取り専用かつdictとインタフェースの近い MappingProxy を採用します。

# how to install

```
$ pip install -e .
```

# test

```
$ pytest
```
