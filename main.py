import requests

url = "https://twitter.com/i/api/graphql/eS7LO5Jy3xgmd3dbL044EA/UserTweets"
headers = {
    "authorization": "Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA",
    "x-csrf-token": "854abebead646758e5e287464e079df9fd07b4cf1625857bfaf101cd022c39070f3570335efde761b3236afbfed0e78a666382f4f4686a679cb674cb15d989146a55cb28f03e6da2baa3200da05f230a",
    "cookie": "guest_id=v1%3A171057328966802917; twtr_pixel_opt_in=Y; d_prefs=MToxLGNvbnNlbnRfdmVyc2lvbjoyLHRleHRfdmVyc2lvbjoxMDAw; guest_id_ads=v1%3A171057328966802917; guest_id_marketing=v1%3A171057328966802917; personalization_id=\"v1_lX+MxD2CsRsdvRzeUb+oCg==\"; _ga=GA1.2.841005914.1710580924; _gid=GA1.2.1062196593.1710580924; g_state={\"i_l\":0}; kdt=fVynpO7riQinGq5NF7qLfR8lmBTeg3gDTRCNUR9g; lang=en; dnt=1; ads_prefs=\"HBISAAA=\"; _twitter_sess=BAh7DiIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCL9qq0aOAToMY3NyZl9p%250AZCIlNzFhMjNkOTY1MzFkMzk0OGRjNTMxNWI0NTU0MmNjYzY6B2lkIiVhMWZj%250ANGQwMWQyZGM2ZTNlOWNiNWVhMjM5Y2Y5N2MzZDoJdXNlcmwrCQCwFqQehYwY%250AOghwcnNpDDoIcHJ1bCsJALAWpB6FjBg6CHBybCIreVBUOEpHaE1uAURQbm5Z%250AUlYxYmp3RVZ4YWRPOFQzS25welZsTDE6CHByYWkG--233c10bc78fd71cb489c208b45935f779a5829f1; auth_token=70525a274eb042f937a3bc6a8668b50f754a18f7; ct0=854abebead646758e5e287464e079df9fd07b4cf1625857bfaf101cd022c39070f3570335efde761b3236afbfed0e78a666382f4f4686a679cb674cb15d989146a55cb28f03e6da2baa3200da05f230a; twid=u%3D1768935120298225664"
}

params = {
    "variables": "{\"userId\":\"44196397\",\"count\":20,\"includePromotedContent\":true,\"withQuickPromoteEligibilityTweetFields\":true,\"withVoice\":true,\"withV2Timeline\":true}",
    "features": "{\"responsive_web_graphql_exclude_directive_enabled\":true,\"verified_phone_label_enabled\":false,\"creator_subscriptions_tweet_preview_api_enabled\":true,\"responsive_web_graphql_timeline_navigation_enabled\":true,\"responsive_web_graphql_skip_user_profile_image_extensions_enabled\":false,\"c9s_tweet_anatomy_moderator_badge_enabled\":true,\"tweetypie_unmention_optimization_enabled\":true,\"responsive_web_edit_tweet_api_enabled\":true,\"graphql_is_translatable_rweb_tweet_is_translatable_enabled\":true,\"view_counts_everywhere_api_enabled\":true,\"longform_notetweets_consumption_enabled\":true,\"responsive_web_twitter_article_tweet_consumption_enabled\":true,\"tweet_awards_web_tipping_enabled\":false,\"freedom_of_speech_not_reach_fetch_enabled\":true,\"standardized_nudges_misinfo\":true,\"tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled\":true,\"rweb_video_timestamps_enabled\":true,\"longform_notetweets_rich_text_read_enabled\":true,\"longform_notetweets_inline_media_enabled\":true,\"responsive_web_enhance_cards_enabled\":false}"
}


def find_full_text(obj):
    full_texts = []
    if isinstance(obj, dict):
        for key, value in obj.items():
            if key == "full_text":
                full_texts.append(value)
            else:
                full_texts.extend(find_full_text(value))
    elif isinstance(obj, list):
        for item in obj:
            full_texts.extend(find_full_text(item))
    return full_texts


def main():
    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    full_texts = find_full_text(data)

    for i in range(10):
        print(f'{i + 1}. {full_texts[i + 1]}')


if __name__ == '__main__':
    main()
