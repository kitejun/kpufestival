Kakao.init('5f2d23cd2c499b2da83462fb37ae738e');
  function sendLink() {
    Kakao.Link.sendDefault({
      objectType: 'feed',
      content: {
        title: '학과: {{intro_detail.dename}}',
        description: '소개: {{ intro_detail.tag }}',
        imageUrl: 'http://kpufestival.waytech.kr/{{ intro_detail.img1.url }}/',
        link: {
          mobileWebUrl: 'http://kpufestival.waytech.kr/intro/intro_detail/{{ intro_detail.id }}/',
          webUrl: 'http://kpufestival.waytech.kr/intro/intro_detail/{{ intro_detail.id }}/',
        }
      },
    });
  }