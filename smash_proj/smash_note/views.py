from django.urls import reverse_lazy
from django.views import generic
#from django.views.generic.edit import CreateView
from .models import Character,MatchResult
from .forms import MatchResultForm
from django.shortcuts import get_object_or_404 # get_object_or_404をインポート
from django.contrib.auth.mixins import LoginRequiredMixin#アクセス制御
from django.core.exceptions import PermissionDenied#Updateで使う

from django.shortcuts import render
from django.http import HttpResponse


from django.contrib.auth.mixins import LoginRequiredMixin#アクセス制御
#Create your views here.
class CharacterSelect(generic.ListView):
    model = Character#表示させるなら横６スマホ？pc１０？
class CharacterDetailView(generic.DetailView):
    model = Character#テンプレート名を省略しているので、Character_detail.htmlが対応される
    template_name = 'smash_note/character_detail.html'
    # context_object_name = 'characters_detail'
    # queryset = Character.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #↓これでhtml上でmatch_resultsとかけばmatch_resultsを呼び出せる
        context['match_results'] = MatchResult.objects.filter(author=self.request.user)#authorが現在のログインユーザーであるオブジェクトのみをフィルタリングしています
        character = self.object
        match_results = MatchResult.objects.filter(opponent_character_id=character)
        #wins = match_results.filter(player_character_id=character, win_flag=True).count()
        wins = match_results.filter(opponent_character_id=character, win_flag=True).count()
        losses = match_results.filter(opponent_character_id=character, win_flag=False).count()
        total_matches = match_results.count()
        nocon = total_matches-wins-losses
        win_rate = round(wins / (wins+losses) * 100) if total_matches != 0 else 0
        context['wins'] = wins
        context['losses'] = losses
        context['total_matches'] = total_matches
        context['win_rate'] = win_rate
        context['nocon']=nocon
        #print(context)
        return context


class MemoCreateView(LoginRequiredMixin,generic.edit.CreateView):
    model=MatchResult

    #template_name = 'smash_note/character_detail.html'
    #fields= '__all__'
    fields = ['player_character_id','opponent_character_id','win_flag','memo']
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super(MemoCreateView,self).form_valid(form)


class MemoCreateView2(generic.CreateView): # MemoCreateViewを定義し、CreateViewを継承する
    model = MatchResult # モデルにMatchResultを指定
    fields = ['player_character_id','win_flag', 'memo'] # フォームのフィールドにwin_flagとmemoを指定
    template_name = 'smash_note/MatchResult_form.html' # テンプレートの名前を指定
    def form_valid(self, form): # フォームが妥当かどうかを検証するためのメソッド
        form.instance.author = self.request.user # ログインユーザーをauthorに追加
        form.instance.opponent_character_id = get_object_or_404(Character, pk=self.kwargs['pk']) # urlのpkからキャラクターを取得し、player_character_idに追加
        return super().form_valid(form) # 親クラスのメソッドを呼び出し、返り値を返す

class MemoUpdateView(LoginRequiredMixin,generic.UpdateView):
    model = MatchResult

    fields=  ['player_character_id','win_flag','memo']

    def dispatch(self,request,*args,**kwargs):#dispatchメソッドをオーバーライド
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied("You do not have permission to edit.")
        return super(MemoUpdateView,self).dispatch(request,*args,**kwargs)

class MemoDeleteView(generic.DeleteView):
    model = MatchResult
    template_name = 'smash_note/matchresult_confirm_delete.html'
    #success_url = reverse_lazy('smash_note:character_index')
    #success_url = reverse_lazy('smash_note:character_detail')
    def get_success_url(self):
        #return reverse_lazy('smash_note:character_detail', kwargs={'pk': self.object.pk})
        #print("\n" ,self,"\n")
        return reverse_lazy('smash_note:character_detail', kwargs={'pk': self.object.opponent_character_id.pk})




def get_character_stats(character):
    matches_as_opponent = MatchResult.objects.filter(opponent_character_id=character.id)
    total_matches = matches_as_opponent.count() + MatchResult.objects.filter(player_character_id=character.id).count()
    wins_as_player = MatchResult.objects.filter(player_character_id=character, win_flag=True).count()
    win_rate = wins_as_player / total_matches * 100 if total_matches > 0 else 0
    stats = {'total_matches': total_matches, 'wins': wins_as_player, 'win_rate': win_rate}
    #return stats
    return HttpResponse(matches_as_opponent)


# def my_view(request):
#     character = Character.objects.first()
#     context = {
#         'character': character,
#         'get_win': get_win,
#     }
#     return render(request, 'my_template.html', context)

# def get_win(num):
#     me_win = MatchResult.objects.filter(opponent_character_id = num)
#     # return HttpResponse(me_win)
#     win_count = me_win.count()
#     return win_count
def num():
    return HttpResponse(2)